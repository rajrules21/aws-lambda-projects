#import required libraries
import boto3
import sys

#create s3 bucket
def create_s3_bucket(bucket_name,region):
    s3 = boto3.client('s3', region_name=region)

    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
            
        )
        print(f"Bucket '{bucket_name}' created succesfully")
        return response
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return None
    
    
#check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python create-s3-bucket.py <bucket_name> <region>")
    sys.exit(1)
    
#Assign command line values to variables
bucket_name = sys.argv[1]
region = sys.argv[2]

#call the function to create buucket
create_s3_bucket(bucket_name, region)
    
        