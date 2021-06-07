import boto3, argparse
import sys
import json

# Connections with s3
s3_client = boto3.client('s3')

BUCKET_NAME = 'simian-scania-prod-output-temp'
#bucket = s3.Bucket(BUCKET_NAME)

def s3_del(Prefix='', Delimiter='/'):
    result = s3_client.list_object_versions(
                                        Bucket=BUCKET_NAME,
                                        Prefix=Prefix,
                                        Delimiter='/'
                                        )

    # CommonPrefixes key has all the sub folders in current directory
    common_prefixes = result.get('CommonPrefixes')

    delete_marked_files = result.get('DeleteMarkers')

    if delete_marked_files:
        for delete_marked_file in delete_marked_files:
            #Delete the delete marker
            response = s3_client.delete_object(
                Bucket=BUCKET_NAME,
                Key=delete_marked_file['Key'],
                VersionId=delete_marked_file['VersionId']
            )

    else:
        print('No deleted files found in folder>>')
        print(Prefix)
    if common_prefixes:
        for common_prefix in common_prefixes:
            folder = common_prefix.get('Prefix')
            # Recursively call init function to go into all sub folders
            s3_del(Prefix=folder)

s3_del(Prefix='enter-your-prefix')
