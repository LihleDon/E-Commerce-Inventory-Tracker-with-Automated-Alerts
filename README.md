# AWS Inventory Checker

An AWS-based system to monitor inventory and send email alerts for low stock.

## Architecture
- **S3**: Stores `inventory.json` in `aws-project-inventory-bucket`
- **Lambda**: `InventoryChecker` checks stock hourly
- **SNS**: `LowStockAlerts` emails `myemail@example.com` when `quantity < 10`
- **CloudWatch**: Triggers Lambda every hour

## Setup
1. **S3**: `aws s3 mb s3://aws-project-inventory-bucket --region af-south-1`
2. **SNS**: `aws sns create-topic --name LowStockAlerts --region af-south-1`
3. **Lambda**: Deploy `lambda_function.py` (see below)
4. **CloudWatch**: Schedule with `aws events put-rule`

## Files
- `inventory.json`: Sample inventory data
- `lambda_function.py`: Lambda code
- `trust-policy.json`: IAM role policy

## Usage
- Upload `inventory.json` to S3
- Lambda runs hourly, sending alerts for low stock

## Free Tier
- Uses <1% of AWS Free Tier limits (S3, SNS, Lambda, CloudWatch).