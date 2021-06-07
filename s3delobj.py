import boto3
import logging 

logger = logging.getLogger()
#bucket.object_versions.delete()

def permanently_delete_object(bucket, object_key):
    """
    Permanently deletes a versioned object by deleting all of its versions.
    """
    try:
        bucket.object_versions.filter(Prefix=object_key).delete()
        logger.info("Permanently deleted all versions of object %s.", object_key)
        print("deleting")
    except ClientError:
        logger.exception("Couldn't delete all versions of %s.", object_key)
        raise

def main():
    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket('simian-scania-prod-output-temp')
    object_key = '8qAy2oaqIgp6tFVFrxTya1D9BTrWzIvt'

    permanently_delete_object(s3_bucket, object_key)

if __name__ == "__main__":
    main()


