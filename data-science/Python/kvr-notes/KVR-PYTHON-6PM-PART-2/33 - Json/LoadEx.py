#LoadEx.py
import json
employee = '  {"id":"09", "name": "Rossum", "department":"IT"}  ' # JSON string format
employee_dict = json.loads(employee) # Convert JSON string format to Python dict
print(employee,type(employee))
print(employee_dict,type(employee_dict))