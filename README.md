# The Doctor App

This project is a containerized Python web application that retrieves a secret string from a DynamoDB table and presents it through a web server. It utilizes Docker and Docker Compose for easy setup and deployment.

## Prerequisites

- Docker: Ensure that Docker is installed on your machine.

## Getting Started

To get started with the Doctor, follow the steps below:

1. Clone the repository to your local machine - `git clone git@github.com:daniel570/zesty-challenge.git`

2. Navigate to the project directory.

3. Edit the .env file and set the environment variables for AWS cli credentials and the DynamoDB table name and code name, to be used by the app (you may use dummy values for ID and key since this is a local DB):
   AWS_ACCESS_KEY_ID = "your_access_key_id"
   AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
   AWS_REGION = "us-east-1"
   TABLE_NAME = "dynamodb_table_name"
   CODE_NAME = "dynamodb_code_name"

4. Pull Docker images and start the services by running the following command:

   ```bash
   docker-compose up -d

Alternatively, you can run the `verification.sh` script.

This command will pull the Docker image for the application and local DynamoDB and start both the application and local DynamoDB services.

Once the services are running, you can access the application at http://localhost:5050

## Endpoints

The application exposes the following endpoints:

/health: Returns a JSON response indicating the health of the application.

/secret: Retrieves the secret string from the DynamoDB table and presents it in the response.


## Scaling

This project focuses on running the application and DynamoDB locally for development and testing purposes. When deploying to production or for higher scalability, you'll need to consider appropriate scaling strategies for both the application and DynamoDB, such as using AWS services like Amazon ECS, Amazon EKS, or Amazon DynamoDB Streams.
