import boto3
import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Create EC2 client
    try:
        logger.info("Creating EC2 client")
        ec2 = boto3.client('ec2')
    except Exception as e:
        logger.error(f"Error creating EC2 client: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error connecting to AWS services!')
        }

    # Get information about all running instances
    try:
        logger.info("Describing EC2 instances")
        reservations = ec2.describe_instances()
        instances = reservations['Reservations']
    except Exception as e:
        logger.error(f"Error describing EC2 instances: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error retrieving instance data!')
        }

    # Initialize empty list to store instance data
    instance_data = []

    # Loop through reservations and extract data
    for reservation in instances:
        for instance in reservation['Instances']:
            try:
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']
                instance_state = instance['State']['Name']
                launch_time = instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S')  # Format launch time
                logger.info(f"Processing instance: {instance_id}")
            except Exception as e:
                logger.error(f"Error processing instance data: {e}")
                continue  # Skip to next instance on error

            # Append data to list
            instance_data.append({'InstanceId': instance_id, 'InstanceType': instance_type,'Instance state': instance_state, 'LaunchTime': launch_time})

    # Create S3 client
    try:
        logger.info("Creating S3 client")
        s3 = boto3.client('s3')
    except Exception as e:
        logger.error(f"Error creating S3 client: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error connecting to AWS services!')
        }

    # Convert list to JSON string
    json_data = json.dumps(instance_data)

    # Upload data to S3 bucket
    try:
        logger.info("Uploading data to S3 bucket")
        s3.put_object(Bucket='lambda-project-10', Key='instance_data.json', Body=json_data)
    except Exception as e:
        logger.error(f"Error uploading data to S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error saving instance data!')
        }

    # Log success message
    logger.info('Instance data saved to S3 bucket lambda-project-10')

    return {
        'statusCode': 200,
        'body': json.dumps('Instance data saved successfully!')
    }
