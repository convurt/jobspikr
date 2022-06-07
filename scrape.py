from urllib.request import Request, urlopen

import config

values = """
    {
  "format": "json",
  "size": 50,
  "exclude_duplicates": true,
  "dataset": [
    "job_board",
    "f500"
  ],
  "search_query_json": {
    "bool": {
      "must": [
        {
          "query_string": {
            "fields": [
              "job_title",
              "inferred_job_title"
            ],
            "query": "*"
          }
        },
        {
          "query_string": {
            "default_field": "job_type",
            "query": "\"full time\""
          }
        },
        {
          "query_string": {
            "default_field": "company_name",
            "query": "*"
          }
        },
        {
          "bool": {
            "should": [
              {
                "bool": {
                  "must": [
                    {
                      "query_string": {
                        "fields": [
                          "inferred_country"
                        ],
                        "query": "\"United States\" OR \"USA\" OR \"United States\" OR \"US\""
                      }
                    }
                  ]
                }
              }
            ]
          }
        },
        {
          "exists": {
            "field": "apply_url"
          }
        },
        {
          "exists": {
            "field": "html_job_description"
          }
        },
        {
          "bool": {
            "should": [
              {
                "exists": {
                  "field": "contact_phone_number"
                }
              },
              {
                "exists": {
                  "field": "contact_email"
                }
              }
            ]
          }
        },
        {
          "range": {
            "post_date": {
              "gte": "2022-05-07",
              "lte": "2022-06-07"
            }
          }
        },
        {
          "query_string": {
            "default_field": "inferred_company_type",
            "query": "\"company\""
          }
        },
        {
          "query_string": {
            "default_field": "inferred_skills",
            "query": "\"Web Design\" OR \"Web Development\""
          }
        }
      ],
      "must_not": [
        {
          "query_string": {
            "default_field": "contact_email",
            "query": "\"na\" OR \"NA\" OR \"unspecified\""
          }
        },
        {
          "query_string": {
            "default_field": "contact_phone_number",
            "query": "\"na\" OR \"NA\" OR \"unspecified\""
          }
        },
        {
          "query_string": {
            "default_field": "company_name",
            "query": "Unspecified"
          }
        }
      ]
    }
  }
}
"""

headers = {
  'Content-Type': 'application/json',
  'client_id': config.client_id, # your client_id
  'client_auth_key': config.client_auth_key # your client_auth_key
}
request = Request('https://api.jobspikr.com/v2/data', headers=headers)

response_body = urlopen(request).read()
print(response_body)
