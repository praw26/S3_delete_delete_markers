# S3_remove_delete_markers


If you have a S3 bucket with versioning enabled, a simple delete operation on objects does not delete the objects, rather adds a delete marker to the object. If you wish to restore the S3 bucket with the delete markers on, then you need to remove the delete markers. A simple delete operation cannot remove the delete markers, so you can use 's3 delete_object version_id' instead. This script removes the delete markers to restore the S3 bucket
