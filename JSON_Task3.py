import json

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Apply pretty-printing with the specified settings
pretty_json = json.dumps(sampleJson, indent=2, separators=(", ", " = "))
print(pretty_json)
