import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

# Parse JSON and get the value of key2 key
jsonData = json.loads(sampleJson)
value_of_key2 = jsonData['key2']
print(value_of_key2)
