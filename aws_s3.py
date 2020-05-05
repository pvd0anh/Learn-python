import boto3
import os
import logging
logger = logging.getLogger('backend')

S3_BUCKET_NAME = 'pvdoanh'
S3_REGION_NAME = 'ap-southeast-1'
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET_NAME)


class S3Upload():
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(S3Upload)
        return cls.singleton

    def __init__(self):
        self.s3 = boto3.client('s3')

    # Check bucket exist
    def check_bucket_exist(self, bucket_name):
        try:
            response = self.s3.list_buckets()
            buckets = [bucket['Name'] for bucket in response['Buckets']]
            return bucket_name in buckets
        except Exception as e:
            # logger.error('Check bucket %s ' % e)
            print('Check bucket error: ', e)
            return False

    # Create new bucket
    def create_new_bucket(self, bucket_name):
        self.s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': S3_REGION_NAME
            }
        )

    # Upload file
    # file_path_absolute: on the disk
    # file_path_relative: on the web
    def upload_file_to_s3(self, file_path_absolute, file_path_relative, bucket_name=S3_BUCKET_NAME, acl="public-read"):
        location = "http://{}.s3.amazonaws.com/{}".format(
            S3_BUCKET_NAME, file_path_relative)
        try:
            file = open(file_path_absolute, 'rb')
            data = self.s3.upload_fileobj(
                file,
                bucket_name,
                file_path_relative,
                ExtraArgs={
                    "ACL": acl,
                    # "ContentType": file.content_type
                }
            )
            return location
        except Exception as e:
            logger.error('Upload file  %s ' % e)
            return ''

    # Get url private file
    def get_file_from_s3(self, file_path, bucket_name=S3_BUCKET_NAME, expire_time=3600):
        # Check bucket exist
        if not self.check_bucket_exist(bucket_name):
            return None
        try:
            # generate_presigned_url : get url private file, ex: image link
            url = self.s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': file_path
                },
                ExpiresIn=expire_time)
            return url
        except Exception as e:
            logger.error('Get url file %s ' % e)
            return ''

    def delete_file_from_s3(self, file_path, bucket_name=S3_BUCKET_NAME):
        # Check bucket exist
        if not self.check_bucket_exist(bucket_name):
            return None
        try:
            # generate_presigned_url : get url private file, ex: image link
            response = self.s3.delete_object(
                Bucket=bucket_name,
                Key=file_path
            )
            return response.DeleteMarker
        except Exception as e:
            logger.error('Delete file %s ' % e)
            return ''


def test():
    uploader = S3Upload()
    print(uploader.s3)

    if S3Upload.singleton:
        uploader = S3Upload.singleton
    else:
        uploader = S3Upload()

    thumbnail_path = '/test/test.jpg'
    thumbnail_url = 'test/test.jpg'
    print('Upload thumbnail to s3 %s' % thumbnail_path)

    uploader.upload_file_to_s3(thumbnail_path, thumbnail_url)
    print(uploader.s3)
