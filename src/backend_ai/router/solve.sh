curl -i -X POST    -H "Content-Type:application/json"    -d '{ "payload":[ { "start": 12, "end": 18, "speaker": "darallium", "content": "test payload" }, { "start": 23, "end": 28, "speaker": "darallium", "content": "example payload" } ] }' 'http://127.0.0.1:8000/api/v1/bedrock/summerize/'


