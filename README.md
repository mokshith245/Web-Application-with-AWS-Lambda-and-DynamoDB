# Web Application with AWS Lambda and DynamoDB

## Overview
This project demonstrates a simple web application that integrates AWS Lambda functions with DynamoDB for managing student records. The backend is implemented in Python and provides API endpoints for CRUD operations on student data.

## Features
- Add, update, delete, and retrieve student records
- Serverless backend using AWS Lambda
- Persistent storage with DynamoDB

## Setup Instructions
1. Clone this repository.
2. Set up your AWS credentials and permissions for Lambda and DynamoDB.
3. Deploy the Lambda functions using AWS Console or AWS CLI.
4. Create a DynamoDB table named `Students` with appropriate primary keys.
5. Update the Lambda function code to connect to your DynamoDB table.

## API Endpoints
- `POST /students` - Add a new student
- `GET /students` - Retrieve all students
- `GET /students/{id}` - Retrieve a student by ID
- `PUT /students/{id}` - Update a student
- `DELETE /students/{id}` - Delete a student

## Screenshots

### DynamoDB Table with Sample Records
<img width="1381" height="287" alt="image" src="https://github.com/user-attachments/assets/e6948ab5-a3df-48f6-938f-25e0e862e954" />


### Successful API Requests
<img width="1422" height="810" alt="image" src="https://github.com/user-attachments/assets/51eb1e83-f048-4d87-b006-04bceea7fb3b" />

<img width="1421" height="830" alt="image" src="https://github.com/user-attachments/assets/c57a3e95-4bfd-45e2-9951-813f63b6ca86" />

<img width="1425" height="818" alt="image" src="https://github.com/user-attachments/assets/19495ab6-bb29-462e-aed8-066e677d532d" />

<img width="1409" height="829" alt="image" src="https://github.com/user-attachments/assets/e9848c3a-ac91-452d-a955-84b84ecfa94d" />



## Reflection

### Challenges Faced
- Setting up IAM roles and permissions for Lambda to access DynamoDB securely.
- Debugging Lambda function errors due to missing environment variables or incorrect table names.
- Handling API Gateway integration with Lambda and mapping request/response formats.

### What I Learned
- How to deploy and test AWS Lambda functions using the AWS Console and CLI.
- The basics of DynamoDB, including table creation, primary keys, and CRUD operations.
- Best practices for serverless application development and troubleshooting AWS services.
