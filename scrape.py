from urllib.request import Request, urlopen

values = """
  {
    "size": 50,
    "cursor": 1549411216369936,
    "format": "json",
    "search_query_json": {
      "query_string": {
        "default_field": "job_title",
        "query": "\"web designer\""
      }
    }
  }
"""

headers = {
  'Content-Type': 'application/json',
  'client_id': 'Replace with your client_id',
  'client_auth_key': 'Replace with your client_auth_key'
}
request = Request('https://api.jobspikr.com/v2/data', headers=headers)

response_body = urlopen(request).read()
print(response_body)
