from flask import Flask, jsonify
import boto3
import os

aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
region_name = os.environ.get("AWS_REGION")

app = Flask(__name__)

# Create DynamoDB client
dynamodb = boto3.client('dynamodb',
                        endpoint_url='http://dynamodb:8000',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name)

@app.route('/health')
def health():
    response = {
        "status": "Healthy!",
        "container": "daniel570/zesty-challenge:latest"
    }
    return jsonify(response)

@app.route('/secret')
def secret():
    table_name = 'devops-challenge'
    code_name = 'theDoctor'

    # Retrieve the item from DynamoDB
    response = dynamodb.get_item(
        TableName=table_name,
        Key={
            'codeName': {'S': code_name}
        }
    )

    # Extract the secret string from the response
    item = response.get('Item')
    secret_code = item.get('secretCode').get('S') if item else ''

    result = {
        'codeName': code_name,
        'secretCode': secret_code
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
