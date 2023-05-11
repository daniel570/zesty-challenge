import boto3

# Configure AWS credentials and region
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
aws_region = 'your_dynamodb_region'

# Create DynamoDB client
dynamodb = boto3.client('dynamodb',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region)

table_name = 'devops-challenge'
code_name = 'YOUR_CODENAME'  # Replace with your codename

# Retrieve the item from DynamoDB
response = dynamodb.get_item(
    TableName=table_name,
    Key={
        'codeName': {'S': code_name}
    }
)

# Extract the secret string from the response
item = response.get('Item')
secret_string = item.get('secretCode').get('S') if item else ''

print('Secret String:', secret_string)
