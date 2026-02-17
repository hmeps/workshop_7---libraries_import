import json 
# Python dictionary 
data = { 
"name": "John Doe", 
"age": 30, 
"city": "New York"
} 
# Convert Python object to JSON string 
json_string = json.dumps(data, indent=4) 
print("JSON string:") 
print(json_string) 
# Parse JSON string back to Python object 
parsed_data = json.loads(json_string) 
print("\nParsed data:") 
print(parsed_data) 
# Write JSON to a file 
with open("data.json", "w") as file: 
    json.dump(data, file, indent=4) 
# Read JSON from a file 
with open("data.json", "r") as file: 
    loaded_data = json.load(file) 
print("\nLoaded data from file:") 
print(loaded_data)