# Project-9: Automated EC2 Snapshot Management

## Overview
This project aims to automate the management of Amazon Elastic Compute Cloud (EC2) snapshots based on predefined retention policies. A Lambda function written in Python is triggered periodically to query EC2 instances, create snapshots of their attached Elastic Block Store (EBS) volumes, and manage the lifecycle of snapshots.

## Functionality
The Lambda function performs the following tasks:
- Queries EC2 instances to identify attached EBS volumes.
- Creates snapshots of the attached EBS volumes.
- Manages snapshot lifecycles based on predefined retention policies:
  - Deletes snapshots older than a specified retention period.
  - Retains a certain number of most recent snapshots for each EBS volume.

## Implementation
The solution is implemented using the following AWS services:
- AWS Lambda: Executes the Python code to automate snapshot management.
- Amazon EC2: Provides the compute instances with attached EBS volumes.
- Amazon CloudWatch Events: Triggers the Lambda function based on a scheduled event.

## Getting Started
To deploy and use the automated EC2 snapshot management system:
1. Ensure you have the necessary permissions to create and manage Lambda functions and IAM roles.
2. Deploy the provided Lambda function code using the AWS Management Console, AWS CLI, or AWS SDKs.
3. Configure a Amazon EventBridge schedule to trigger the Lambda function at specified intervals.
4. Verify that the IAM role associated with the Lambda function has the required permissions to describe EC2 instances, create snapshots, and manage snapshot lifecycles.
5. Test the system to ensure snapshots are created and managed as expected.

** Note:- We are not using AWS Cloudwatch Events to trigger the Lambda function since we want the trigger to work on our local time zone and Cloudwatch Events work on UTC timezone offsets.

## Configuration
- Lambda Function: Configure the Lambda function with appropriate environment variables, such as retention periods and snapshot limits.
- Amazon EventBridge Schedules : Customize the schedule for triggering the Lambda function based on your snapshot management requirements.

## Troubleshooting
If the automated snapshot management system encounters errors or does not behave as expected:
- Review CloudWatch Logs for the Lambda function to identify any errors or exceptions.
- Verify IAM permissions for the Lambda function to ensure it has sufficient permissions to perform necessary actions.
- Check CloudTrail logs for API calls and investigate any unauthorized operations or failures.

## Contributing
Contributions to improve the functionality, performance, or documentation of this project are welcome. Please submit a pull request or open an issue on GitHub.


