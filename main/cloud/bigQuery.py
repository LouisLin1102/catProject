from google.cloud import bigquery as bq
from google.cloud import storage 
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "main/catproject-338203-46708b7921f1.json"
bqClient = bq.Client()
stClient = storage.Client()

storage.blob._DEFAULT_CHUNKSIZE = 2097152 # 1024 * 1024 B * 2 = 2 MB
storage.blob._MAX_MULTIPART_SIZE = 2097152 # 2 MB

def QueryDataCount(date):
    queryStr = ("""
    SELECT count(*) FROM `catproject-338203.cat.catLife` WHERE DATE = '{}'
    """).format(date)

    query_job = bqClient.query(queryStr)  # Make an API request.
    print("The query data:")
    print(query_job)
    for row in query_job:
        print(row)
        number = row[0]
    
    return number

def UploadPhoto(sourceFile):
    bucket = stClient.bucket("catlife")
    blob = bucket.blob("temp/image.jpg")
    blobs = bucket.list_blobs(prefix="temp")
    for blob in blobs:
        print(blob.name)
        blob.delete()

    with open(sourceFile, 'rb') as f:
        blob.upload_from_file(f,content_type='image/jpeg')

# UploadPhoto("/home/pi/Public/image.jpg")