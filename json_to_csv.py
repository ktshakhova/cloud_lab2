import boto3
import pathlib
import os
import sys
import json
import csv


with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    headers = data[0].keys()


with open(sys.argv[2], 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for record in data:
        rec = (value for value in record.values())
        writer.writerow(rec)

s3 = boto3.client("s3")
bucket_name = "ktshakhovabucket"
object_name = sys.argv[2]
file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), sys.argv[1])

response = s3.upload_file(file_name, bucket_name, object_name)
print(response)  # prints None
