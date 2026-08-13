# Serverless Task Manager on AWS

A serverless task management web application built and deployed using AWS.

Users can create, view, edit, complete, and delete tasks. The frontend communicates with a REST API that invokes AWS Lambda functions, with task data stored in Amazon DynamoDB.


## Architecture

<img width="1605" height="1013" alt="Project 3 - Severless Task Manager on AWS Diagram" src="https://github.com/user-attachments/assets/b62503ee-3cb9-4626-9aad-1263a3c8a3e3" />


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

<img width="1507" height="873" alt="Task Manager Website-Home" src="https://github.com/user-attachments/assets/832a7895-fcb9-4115-b535-bab21bb5c0c7" />


The frontend is hosted as a static website using Amazon S3 and communicates with API Gateway using JavaScript Fetch API requests.

## API Gateway

<img width="1512" height="830" alt="api-gateway" src="https://github.com/user-attachments/assets/1b7e1f10-1da5-4fe8-a22a-4311851f59e5" />


API Gateway routes HTTP requests from the frontend to the appropriate Lambda function.

## Serverless Backend

Four Lambda functions handle the application's CRUD operations:


- `create-task` — writes new tasks to DynamoDB

<img width="1512" height="622" alt="create-task lambda" src="https://github.com/user-attachments/assets/1b2cf3f2-3a5a-48e3-940a-d363ccf34395" />



- `get-tasks` — retrieves tasks

<img width="1512" height="733" alt="get-task lambda" src="https://github.com/user-attachments/assets/cdfebfb4-ba8f-4069-95f4-69837f874755" />



- `update-task` — updates task information or status

<img width="1510" height="733" alt="update-task lambda" src="https://github.com/user-attachments/assets/5dc42362-b762-4cf3-9c5c-0fbc533985ba" />



- `delete-task` — removes tasks

<img width="1512" height="556" alt="delete-task lambda" src="https://github.com/user-attachments/assets/98b238b2-de77-4bbf-87e7-2b6f1337ab00" />



## Database

<img width="1510" height="758" alt="dynamodb-table" src="https://github.com/user-attachments/assets/87a8362d-9da8-4475-9147-2679ea664991" />

<img width="1512" height="739" alt="dynamodb-items" src="https://github.com/user-attachments/assets/cf14da47-87d2-4bb3-ad2f-2c3341b103ef" />



Amazon DynamoDB stores each task using a unique `taskId` as the partition key.

Each task contains:

- taskId
- title
- description
- status
- createdAt

## Frontend Hosting

<img width="1512" height="829" alt="s3-frontend" src="https://github.com/user-attachments/assets/3922e8b4-25bb-412f-8155-4cad417c4971" />


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
