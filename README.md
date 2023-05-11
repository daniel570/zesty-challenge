# theDoctor

This project is a containerized Python web application that retrieves a secret string from a DynamoDB table and presents it through a web server. It utilizes Docker and Docker Compose for easy setup and deployment.

## Prerequisites

- Docker: Ensure that Docker is installed on your machine.

## Getting Started

To get started with the project, follow the steps below:

1. Clone the repository to your local machine - `git clone git@github.com:daniel570/zesty-challenge.git`

2. Navigate to the project directory.

3. Set environment variables for AWS cli, to be used by the app (you may use dummy values for ID and key since this is a local DB):
   export AWS_ACCESS_KEY_ID=""
   export AWS_SECRET_ACCESS_KEY=""
   export AWS_REGION="us-east-1"

4. Pull Docker images and start the services by running the following command:

   ```bash
   docker-compose up -d

Alternatively, you can run the `verification.sh` script.
