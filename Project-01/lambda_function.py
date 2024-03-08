import boto3
from PIL import Image
import io

destination_bucket_name = "project-1-dest"

def lambda_handler(event, context):
    s3_client = boto3.client("s3")
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = event["Records"][0]["s3"]["object"]["key"]

    # Download original image
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        image = Image.open(response["Body"])
    except Exception as e:
        print(f"Error downloading image: {e}")
        return {"statusCode": 500, "body": "Error downloading image"}

    # Resize image
    resized_width = 600  # Adjust this value as needed
    resized_height = int(image.height * (resized_width / image.width))
    resized_image = image.resize((resized_width, resized_height))

    # Create thumbnail
    thumbnail_width = 150  # Adjust this value as needed
    thumbnail_height = int(image.height * (thumbnail_width / image.width))
    thumbnail = image.resize((thumbnail_width, thumbnail_height))

    # Upload resized and thumbnail images to S3 with different keys
    resized_key = f"resized/{object_key}"
    thumbnail_key = f"thumbnails/{object_key}"

    try:
        # Replace the following with your preferred image format (e.g., JPEG, PNG)
        in_memory_resized = io.BytesIO()
        # After resizing the images:
        resized_image = resized_image.convert('RGB')  # Convert to RGB mode
        resized_image.save(in_memory_resized, format="JPEG")
        s3_client.put_object(Bucket=destination_bucket_name, Key=resized_key, Body=in_memory_resized.getvalue())

        in_memory_thumbnail = io.BytesIO()
        thumbnail = thumbnail.convert('RGB')         # Convert to RGB mode
        thumbnail.save(in_memory_thumbnail, format="JPEG")
        s3_client.put_object(Bucket=destination_bucket_name, Key=thumbnail_key, Body=in_memory_thumbnail.getvalue())

        return {"statusCode": 200, "body": "Image and thumbnail processed successfully"}
    except Exception as e:
        print(f"Error uploading resized image and thumbnail: {e}")
        return {"statusCode": 500, "body": "Error uploading resized image and thumbnail"}
