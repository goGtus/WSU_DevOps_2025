import urllib3

def handler(event, context):
    url = "https://example.com"
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    print(f"Checked {url} - Status Code: {response.status}")
    return {"statusCode": response.status}
