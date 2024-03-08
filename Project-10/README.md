# EC2 Inventory Tracker

## Overview

The EC2 Inventory Tracker is a Lambda function designed to retrieve information about EC2 instances in your AWS account and store it in an S3 bucket. This information includes details such as instance ID, instance type, launch time, and instance state.

## Objectives

- Retrieve information about running EC2 instances.
- Store instance data in an S3 bucket.
- Monitor and track changes in EC2 instances over time.

## Components

- **Lambda Function**: Written in Python 3.12, this function uses the Boto3 library to interact with the AWS SDK and retrieve information about EC2 instances.
- **S3 Bucket**: Used to store the instance data retrieved by the Lambda function.
- **Amazon EventBridge**: Used to invoke Lambda function as per a schedule

## Usage

1. Deploy the Lambda function in your AWS account.
2. Configure the Lambda function to run on a schedule or trigger event using Amazon EventBridge schedule.
3. Ensure the Lambda function has necessary IAM permissions to access EC2 instances and S3 bucket.
4. Monitor CloudWatch Logs for any errors or issues encountered during execution.

## Configuration

- **IAM Role**: Create an IAM role with permissions to access EC2 instances and S3 bucket.
- **S3 Bucket**: Create an S3 bucket to store the instance data.

## Deployment

- Deploy the Lambda function using the AWS Management Console or AWS CLI.
- Configure the Lambda function's trigger or schedule.

## Troubleshooting

- Check CloudWatch Logs for any error messages or issues encountered during execution.
- Ensure the Lambda function has proper permissions to access EC2 instances and S3 bucket.
- Verify that the S3 bucket exists and is accessible.

## License

This project is licensed under the [MIT License](LICENSE).
