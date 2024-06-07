# day30_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

----------------------------
## Password Manager Enchancements
The following enhancements have been made to the Password Manager project:

1. __Switch from txt to JSON Format:__ Data is now stored in a JSON file, making it easier to manage and retrieve structured data.
2. __Search Capability:__ Users can search for saved credentials by entering the website name, and the application will display the associated email and password.
3. __Exception Handling:__ The application handles exceptions such as missing data files and non-existent entries gracefully, providing appropriate error messages to the user.

## Why use Exception Handling?

- __Graceful Failure:__ Your program can handle errors without crashing, providing a better user experience.
- __Custom Error Handling:__ You can specify different actions for different types of errors.
- __Resource Management:__ Ensure resources like files and network connections are properly managed and closed.

## How Exception Handling Works
Exception handling in Python is done using __try__, __except__, __else__, and __finally__ blocks. Here's a breakdown of how each part works:
```python
try:
  # Code that might raise an exception
except ExceptionType:
  # Code to handle the exception
else:
  # Code to execute if no exception occurs
finally:
  # Code to always execute, regardless of exceptions
```
For Example
```python
try:
  # Open a file
  with open("myfile.txt") as file:
    data = file.read()
except FileNotFoundError:
  print("Error: File not found!")
else:
  print(f"File contents: {data}")
finally:
  # Close the file if it was opened successfully
  if file:
    file.close()
```
## Working with JSON in Python:
- json.dump
- json.read
- json.update

**Writing JSON Data: json.dump**
The __json.dump__ method is used to write JSON data to a file. It serializes a Python object into a JSON formatted stream and writes it to a file.
```python
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

**Reading JSON Data: json.load**
The __json.load__ method is used to read JSON data from a file and deserialize it into a Python object.
```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

**Updating JSON Data**
To update JSON data, you typically load the existing JSON data into a Python dictionary, make your updates, and then write the updated dictionary back to the JSON file.
```python
import json

# Load existing data
with open('data.json', 'r') as file:
    data = json.load(file)

# Update the data
data['age'] = 31
data['email'] = 'john.doe@example.com'

# Write updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```









