import boto3
import json

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        event_name = record['eventName']
        
        if event_name.startswith('ObjectCreated'):
            send_email_notification(bucket_name, object_key, event_name)
        elif event_name.startswith('ObjectRemoved'):
            send_email_notification(bucket_name, object_key, event_name)

def send_email_notification(bucket_name, object_key, event_name):
    subject = f"S3 Event Notification: {event_name}"
    message_text = f"An event ({event_name}) occurred in S3 bucket {bucket_name}. Object key: {object_key}"
    message_html = f"<p>An event ({event_name}) occurred in S3 bucket {bucket_name}.</p><p>Object key: {object_key}</p>"
    sender_email = "princealexster@gmail.com"  # Update with your sender email
    recipient_email = "rajrules21@gmail.com"  # Update with recipient email

    try:
        response = ses_client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [
                    recipient_email,
                ]
            },
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': message_text},
                    'Html': {'Data': message_html}
                }
            }
        )
        print("Email sent successfully:", response['MessageId'])
    except Exception as e:
        print("Error sending email:", str(e))

