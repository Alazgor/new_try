import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Let's parse the JSON and get the value of the "salary" key.
jsonData = json.loads(sampleJson)
salary_value = jsonData['company']['employee']['payble']['salary']
print(salary_value)