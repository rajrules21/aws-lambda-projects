import boto3
from datetime import datetime, timedelta

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    # Get the current time in IST
    ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)

    # Define retention period for snapshots (in days)
    retention_days = 7

    # Get a list of all EC2 instances
    instances = ec2_client.describe_instances()

    # Iterate through each instance
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']

            # Create snapshots for attached EBS volumes
            for volume in instance['BlockDeviceMappings']:
                volume_id = volume['Ebs']['VolumeId']
                snapshot_description = f"Snapshot for volume {volume_id} of instance {instance_id}"
                create_snapshot(volume_id, snapshot_description)

    # Manage snapshot lifecycles based on retention policy
    manage_snapshot_lifecycle(retention_days)

def create_snapshot(volume_id, description):
    try:
        response = ec2_client.create_snapshot(
            VolumeId=volume_id,
            Description=description
        )
        print("Snapshot created:", response['SnapshotId'])
    except Exception as e:
        print("Error creating snapshot:", str(e))

def manage_snapshot_lifecycle(retention_days):
    try:
        snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']
        for snapshot in snapshots:
            snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
            if datetime.utcnow() - snapshot_time > timedelta(days=retention_days):
                ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
                print("Snapshot deleted:", snapshot['SnapshotId'])
    except Exception as e:
        print("Error managing snapshot lifecycle:", str(e))
