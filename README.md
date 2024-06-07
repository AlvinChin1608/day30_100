# day30_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

----------------------------
## Password Manager Enchancements
The following enhancements have been made to the Password Manager project:

1. Switch from txt to JSON Format: Data is now stored in a JSON file, making it easier to manage and retrieve structured data.
2. Search Capability: Users can search for saved credentials by entering the website name, and the application will display the associated email and password.
3. Exception Handling: The application handles exceptions such as missing data files and non-existent entries gracefully, providing appropriate error messages to the user.

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
