## Summary
Reads the messages/events from kafka topic and fetches the images from corresponding cloud storage environment.
Analyze the downloaded image and saves the data into mongo db for search algorithm.

#### Configuguring Environmental variables
- `CONFIDENCE_THRESHOLD` which is the threshold for determining the object. By default the value is set to '0.6'
- `CLOUD_STORAGE_TYPE` determines the type of cloud storage used 
    - set 'aws' if you want to configure it to s3
    - set 'azure' if you want to configure it to Azure Blob
- 'AZURE_ACCOUNT_NAME' 
- 'AZURE_ACCOUNT_KEY'
- 'AWS_ACCESS_KEY_ID'
- 'AWS_SECRET_ACCESS_KEY'

#### Note: 
- `requirements.txt` contains the required pip module which needs to be installed.
- `kafka_consumer.py` file is the entry point of the applicaiton which will be in a never ending loop