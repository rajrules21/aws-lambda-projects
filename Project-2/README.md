# S3 Event Notification System with SES

This project demonstrates how to create an automated system that sends email notifications whenever certain events occur in an Amazon S3 bucket using Amazon Simple Email Service (SES) and AWS Lambda.

## Overview

Amazon S3 provides event notifications that can trigger AWS Lambda functions in response to various bucket events such as object creation and deletion. This project utilizes S3 event notifications to trigger a Lambda function, which in turn sends email notifications using Amazon SES.

## Objectives

- Configure S3 event notifications to trigger Lambda functions on specific bucket events (e.g., object creation, deletion).
- Write a Lambda function in Python to handle S3 events and send email notifications using SES.
- Customize the email notification content to include relevant information about the S3 event.
- Test the end-to-end workflow by uploading/deleting objects in the S3 bucket and verifying email notifications.
- Deploy the Lambda function and associated resources to the AWS account.

## Technologies Used

- AWS Lambda
- Amazon S3
- Amazon SES
- Python (for Lambda function code)

## Getting Started

1. **Set up AWS Account:**
   - If you haven't already, sign up for an AWS account at https://aws.amazon.com/.

2. **Configure AWS Credentials:**
   - Set up AWS CLI or AWS SDK with credentials for accessing your AWS account.

3. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/s3-event-notification.git


## Steps:

1. Customize Lambda Function:

Modify the Lambda function code (lambda_function.py) to customize email content and recipient details.

2. Configure S3 Event Notifications:

Set up event notifications on the S3 bucket(s) of interest to trigger the Lambda function on specific events (e.g., object creation, deletion).

3. Verify Email Addresses:

Verify sender and recipient email addresses in the Amazon SES console to ensure successful email delivery.

4. Deploy Lambda Function:

Package the Lambda function code and dependencies into a deployment package.
Deploy the Lambda function to your AWS account using AWS CLI or AWS Management Console.

5. Test Functionality:

Upload/delete objects in the S3 bucket to trigger events and verify that email notifications are sent successfully.