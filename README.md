# E-Commerce Inventory Tracker with Automated Alerts

A serverless AWS solution to monitor e-commerce inventory and send real-time email alerts for low stock levels, built with a passion for efficient data workflows and cloud automation.

## Purpose
This project tracks inventory stored in an S3 bucket and uses AWS Lambda to check stock levels hourly. If any item falls below a threshold (10 units), it triggers an SNS email alert. Designed with simplicity and scalability in mind, it showcases practical skills in AWS data engineering and automation.

## Architecture
- **Amazon S3**: Stores `inventory.json` in `aws-project-inventory-bucket`.
- **AWS Lambda**: `InventoryChecker` processes inventory data hourly.
- **Amazon SNS**: `LowStockAlerts` sends email notifications to `myemail@example.com`.
- **CloudWatch Events**: Schedules Lambda execution every hour.

## Key Features
- **Automated Monitoring**: Runs 24/7 with zero manual intervention.
- **Cost-Efficient**: Stays within AWS Free Tier limits.
- **Scripted Deployment**: Built and managed via PowerShell and AWS CLI.

## Setup Instructions
1. **S3 Bucket**: `aws s3 mb s3://aws-project-inventory-bucket --region af-south-1`
2. **SNS Topic**: `aws sns create-topic --name LowStockAlerts --region af-south-1`
3. **Lambda Function**: Deploy `lambda_function.py` with required IAM role (see `trust-policy.json`).
4. **CloudWatch Schedule**: `aws events put-rule --name RunInventoryCheckerHourly --schedule-expression "rate(1 hour)"`

## Files
- `inventory.json`: Sample inventory data (e.g., T-shirts: 5 units).
- `lambda_function.py`: Lambda function code.
- `trust-policy.json`: IAM trust policy for Lambda execution.
- `README.md`: This documentation.

## How It Works
1. Upload `inventory.json` to S3.
2. Lambda runs hourly, parsing the JSON and checking quantities.
3. SNS emails alerts for items with <10 units (e.g., "Low stock alert: T-shirt (ID: 123) has 5 units left!").

## AWS Free Tier Usage
- **S3**: ~183 bytes (< 5 GB).
- **SNS**: 1 email (< 1,000/month).
- **Lambda**: ~720 seconds/month (< 750,000 seconds).
- **CloudWatch**: Basic scheduling (free).

## Skills Demonstrated
- AWS service integration (S3, Lambda, SNS, CloudWatch).
- PowerShell scripting for cloud automation.
- Python for data processing in Lambda.
- Interest in scalable, data-driven solutions.

## Next Steps
Exploring enhancements like DynamoDB for real-time inventory updates or Athena for analytics—areas I’m eager to dive deeper into as an AWS data enthusiast.

---
Created by LihleDon | GitHub: https://github.com/LihleDon