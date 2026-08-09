# Serverless Task Manager on AWS

A serverless task management web application built and deployed using AWS.

Users can create, view, edit, complete, and delete tasks. The frontend communicates with a REST API that invokes AWS Lambda functions, with task data stored in Amazon DynamoDB.

## Architecture

![Architecture Diagram](screenshots/architecture.png)

### Request Flow

User → S3 Frontend → API Gateway → AWS Lambda → DynamoDB

## AWS Services Used

- Amazon S3 — hosts the static HTML frontend
- Amazon API Gateway — provides REST API endpoints
- AWS Lambda — executes backend CRUD operations
- Amazon DynamoDB — stores task data
- AWS IAM — provides least-privilege permissions for Lambda functions
- Amazon CloudWatch — Lambda logging and monitoring

## Features

- Create new tasks
- Retrieve stored tasks
- Edit task titles and descriptions
- Mark tasks as complete
- Delete tasks
- Persistent task storage using DynamoDB

## REST API

| Method | Endpoint | Function |
|---|---|---|
| GET | /tasks | Retrieve all tasks |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Application

![Task Manager](screenshots/task-manager.png)

The frontend is hosted as a static website using Amazon S3 and communicates with API Gateway using JavaScript Fetch API requests.

## API Gateway

![API Gateway](screenshots/api-gateway.png)

API Gateway routes HTTP requests from the frontend to the appropriate Lambda function.

## Serverless Backend

![Lambda Functions](screenshots/lambda-functions.png)

Four Lambda functions handle the application's CRUD operations:

- `create-task` — writes new tasks to DynamoDB
- `get-tasks` — retrieves tasks
- `update-task` — updates task information or status
- `delete-task` — removes tasks

## Database

![DynamoDB](screenshots/dynamodb.png)

Amazon DynamoDB stores each task using a unique `taskId` as the partition key.

Each task contains:

- taskId
- title
- description
- status
- createdAt

## Frontend Hosting

![S3](screenshots/s3-frontend.png)

The frontend consists of a static `index.html` file hosted using Amazon S3 static website hosting.

## Security

AWS IAM execution roles provide the Lambda functions with only the DynamoDB permissions required for their operations, such as `PutItem`, `Scan`, `UpdateItem`, and `DeleteItem`.

## What I Learned

This project gave me hands-on experience with:

- Building a serverless AWS architecture
- Creating REST API endpoints with API Gateway
- Connecting API Gateway to Lambda
- Using Python and Boto3 to interact with DynamoDB
- Configuring IAM permissions
- Implementing CRUD operations
- Configuring CORS for browser API requests
- Hosting a static frontend with Amazon S3
- Troubleshooting AWS service integrations

## Architecture Summary

S3 serves the frontend application. JavaScript sends HTTP requests to API Gateway, which routes each request to the appropriate Lambda function. The Lambda functions use Boto3 to perform CRUD operations against the DynamoDB Tasks table.
