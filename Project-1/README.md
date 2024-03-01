# Image Processing with AWS Lambda + S3

This project demonstrates how to automate image processing tasks using AWS Lambda and Amazon S3. When an image is uploaded to an S3 bucket, a Lambda function is triggered to perform various image processing operations such as resizing, cropping, and thumbnail creation.

## Overview

The project utilizes AWS Lambda, a serverless compute service, along with Amazon S3 (Simple Storage Service) for storage of images. When an image is uploaded to a designated S3 bucket, an event triggers a Lambda function, which performs the defined image processing tasks. This enables scalable and efficient image processing without the need for managing server infrastructure.

## Objectives

- Set up AWS environment including IAM roles and permissions.
- Create an AWS Lambda function to handle image processing tasks.
- Configure S3 bucket events to trigger the Lambda function upon image upload.
- Define and implement image processing operations such as resizing and thumbnail creation.
- Test the Lambda function with sample images to ensure proper functionality.
- Deploy the Lambda function and associated resources to the AWS account.

## Technologies Used

- AWS Lambda
- Amazon S3
- Python 3.12 (for Lambda function code)
- Pillow (Python Imaging Library) for image processing

## Getting Started

1. **Set up AWS Account:**
   - If you haven't already, sign up for an AWS account at https://aws.amazon.com/.

2. **Configure AWS Credentials:**
   - Set up AWS CLI or AWS SDK with credentials for accessing your AWS account.

3. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/aws-lambda-image-processing.git
