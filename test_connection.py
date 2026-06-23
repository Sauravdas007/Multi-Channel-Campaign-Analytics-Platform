from google.cloud import bigquery

client = bigquery.Client()

print("Connected successfully!")
print("Project:", client.project)