import json
import boto3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from tempfile import mkdtemp
import os
import time

def lambda_handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('JobScrapedata')

    # Get the job_id from the event
    job_id = event.get('job_id')
    if not job_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Job ID not provided"})
        }

    # Chrome options for headless operation
    chrome_service = Service("/opt/chromedriver")
    chrome_options = Options()
    chrome_options.binary_location = '/opt/headless-chromium'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280x1696")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        # Open the LinkedIn job page
        job_url = f"https://www.linkedin.com/jobs/view/{job_id}/"
        driver.get(job_url)

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "modal__overlay"))
        )

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/button'))
        )
        element.click()

        # Wait for the page to load and scrape job details
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'top-card-layout__title'))
        )
        job_title = driver.find_element(By.CLASS_NAME, 'top-card-layout__title').text
        company_name = driver.find_element(By.CSS_SELECTOR, '.topcard__org-name-link.topcard__flavor--black-link').text
        job_location = driver.find_element(By.CSS_SELECTOR, '.topcard__flavor.topcard__flavor--bullet').text

        # Click 'Show More' to reveal job description
        show_more = driver.find_element(By.CSS_SELECTOR, "button[aria-label='i18n_show_more']")
        show_more.click()
        job_description = driver.find_element(By.CSS_SELECTOR, '.show-more-less-html__markup.relative.overflow-hidden').text

        # Format job description
        formatted_job_description = job_description.replace("\\n", "\n")

        # Structure data in JSON format
        job_data_tree = {
            "job_id": job_id,
            "job_title": job_title,
            "company": {
                "name": company_name,
                "location": job_location
            },
            "job_description": {
                "overview": formatted_job_description.split('\n')[0],
                "details": "\n".join(formatted_job_description.split('\n')[1:])
            }
        }

        # Save data to DynamoDB
        table.put_item(Item=job_data_tree)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Job details saved to DynamoDB successfully", "data": job_data_tree}, ensure_ascii=False, indent=3)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    finally:
        driver.quit()
