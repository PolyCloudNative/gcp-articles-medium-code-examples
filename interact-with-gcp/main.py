import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/rtiwaripoc/Desktop/CODE/.keys/umeeyserverless-da25a4d4038a.json'

# Instantiates a client
storage_client = storage.Client()

# Creates the bucket with the specified name
bucket_name = 'umeey03'
bucket = storage_client.create_bucket(bucket_name)

print(f'Bucket {bucket.name} created.')
