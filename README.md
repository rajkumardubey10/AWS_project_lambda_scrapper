# Serverless Job Data Scraper: Scalable and Resilient AWS-Powered Solution for Freelance Client

## Project Overview
This project implements a robust and scalable serverless system to scrape job details from LinkedIn. The system uses AWS Lambda for executing scraping tasks and is triggered via API Gateway. It leverages Selenium with a headless browser and proxy rotation to efficiently scrape job details. The scraped data is stored in DynamoDB in JSON format.
The solution is designed to handle high-volume requests, ensuring scalability, reliability, and performance.

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
