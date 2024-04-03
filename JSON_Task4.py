import json

sampleJson = {"id": 1, "name": "value2", "age": 29}

# Sort JSON keys in alphabetical order
sorted_json = json.dumps(sampleJson, indent=4, sort_keys=True)

print(sorted_json)
