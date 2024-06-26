"""
B2.
"""

import boto3
import botocore

from .s3 import S3Client


class B2Client(S3Client):
    scheme = "b2"
