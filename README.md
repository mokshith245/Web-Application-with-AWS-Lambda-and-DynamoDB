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
![DynamoDB Table Screenshot](screenshots/dynamodb-table.png)

### Successful API Requests
![API Request Screenshot](screenshots/api-success.png)

_Place your screenshots in the `screenshots/` folder and update the image paths above as needed._

## Reflection

### Challenges Faced
- Setting up IAM roles and permissions for Lambda to access DynamoDB securely.
- Debugging Lambda function errors due to missing environment variables or incorrect table names.
- Handling API Gateway integration with Lambda and mapping request/response formats.

### What I Learned
- How to deploy and test AWS Lambda functions using the AWS Console and CLI.
- The basics of DynamoDB, including table creation, primary keys, and CRUD operations.
- Best practices for serverless application development and troubleshooting AWS services.

---

Feel free to update this README with more details about your implementation, architecture diagrams, or additional screenshots as needed.