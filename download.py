import sys
import boto3

s3 = boto3.client('s3')
s3.download_file('ktshakhovabucket', sys.argv[1], sys.argv[1])
