import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    bucket = 'aws-project-inventory-bucket'
    key = 'inventory.json'
    topic_arn = 'arn:aws:sns:af-south-1:203918881738:LowStockAlerts'

    # Get the inventory file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    inventory = json.loads(response['Body'].read().decode('utf-8'))

    # Check each product
    for item in inventory:
        if item['quantity'] < 10:
            message = f"Low stock alert: {item['name']} (ID: {item['product_id']}) has {item['quantity']} units left!"
            sns.publish(TopicArn=topic_arn, Message=message)

    return {
        'statusCode': 200,
        'body': json.dumps('Inventory checked')
    }