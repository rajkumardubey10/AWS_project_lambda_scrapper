# Serverless Job Data Scraper: Scalable and Resilient AWS-Powered Solution for Freelance Client

## Project Overview
This project implements a robust and scalable serverless system to scrape job details from LinkedIn. The system uses AWS Lambda for executing scraping tasks and is triggered via API Gateway. It leverages Selenium with a headless browser and proxy rotation to efficiently scrape job details. The scraped data is stored in DynamoDB in JSON format.
The solution is designed to handle high-volume requests, ensuring scalability, reliability, and performance.

![Python 3.9](https://img.shields.io/badge/Python-3.9-yellow.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.27.1-drakgreen.svg)
![ChromeDriver](https://img.shields.io/badge/ChromeDriver-115+-red.svg)
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-Python3.9-FF9900.svg)
![AWS API Gateway](https://img.shields.io/badge/AWS_API_Gateway-REST_API-FF4F00.svg)
![AWS DynamoDB](https://img.shields.io/badge/AWS_DynamoDB-NoSQL_Storage-4053D6.svg)
![AWS Serverless](https://img.shields.io/badge/AWS_Serverless-Framework-blue.svg)
![Postman](https://img.shields.io/badge/Postman-API_Tests-orange.svg)



## Project Architecture

![AWS_Project_Architectures  (1)](https://github.com/user-attachments/assets/a2c1ac3d-0d48-4a77-9ec8-9502fdc2c7c3)

1 **Input Trigger:** The API Gateway receives POST requests containing the LinkedIn Job ID.

2 **Lambda Function:**
- Scrapes the LinkedIn job page using Selenium.
- Handles CAPTCHA and other anti-scraping measures using proxy rotation.
  
3 **Data Storage:** The scraped job details are stored in DynamoDB in JSON format.

4 **Output:** The response includes the job details or an error message if the scraping fails.

## Prerequisites
### Tools and Services
- AWS Account
- Python 3.9+
- AWS CLI or Serverless Framework
- Postman
- Selenium 4+ Version

  ## File Structure

```plaintext
.
├── LICENSE                     # License file for the project
├── README.md                   # Project documentation
├── aws_project_architecture/   # Folder containing architecture diagrams
│   └── AWS_Project_Architectures. (1).jpeg
├── aws_screenshots/            # Folder containing screenshots of AWS services
│   ├── dynamodbshot.png
│   ├── dynamoshot.png
│   ├── lambdashot.png
│   └── postmanshot.png
├── dependences/                # Dependencies folder with required tools
│   ├── Chrome.zip
│   └── selenium.zip
├── dynamo.py                   # Script for DynamoDB-related operations
├── lambda_function.py          # Main Lambda function script
├── lambda_function.zip         # Compressed Lambda function for deployment
└── requirements.txt            # List of Python dependencies 
```

## Technical Stack
- **Programming Language:** Python
- **Web Scraping:** Selenium in headless browser mode with proxy rotation.
- **Deployment:** AWS Lambda with dependencies managed as Lambda layers.
- **Database:** AWS DynamoDB for storing job details in JSON format.
- **API Trigger:** AWS API Gateway with **Postman** for testing.

## Screenshots
1. Lambda Function
- In Lambda Function I have uploaded all dependences as zip format in lambda layers.
- And here I use the S3 bucket for uploading the zip file because in lambda there is a file limit for uploading the zip file so I have used the S3 bucket for dependencies
- Here I have uploaded the screenshot of successfully run the code and getting the output as scrape data.
  
![lambdashot](https://github.com/user-attachments/assets/3d3e4356-d6ef-4aad-b00a-17d88aecc6be)

2. Postman and API Gateway
- Here I have used the API Gateway URL for sending the request from postman to API Gateway for Triggering the lambda Function.
- And I have Tried testing with different JOB IDs and it is working fine.
    
![postmanshot](https://github.com/user-attachments/assets/cf01d9cb-efd1-41f5-9eaa-04d6c386116c)

3. DynamoDB Table
Create a DynamoDB table with the following schema:
- Primary Key: JobID
- Attributes: Title, Description, Company, Location.
- Here below I have attached the example of screenshot after running how the scrape data has been store and looks in json in DynamoDB

1st  ![dynamodbshot](https://github.com/user-attachments/assets/6c23be3e-c904-484b-b01a-1821ab6fc5ad)

2nd ![dynamoshot](https://github.com/user-attachments/assets/d3a702be-483b-46e9-8c1f-97cd86c89d09)
