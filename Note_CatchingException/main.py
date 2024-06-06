# Catching Exception
"""
When something go wrong, in that moment we catch that exception, then it doesn’t have to fail catastrophically.
So, it can fail more gracefully or we can decide that something else should happen.

Here is how the code will look like

Try: execute something that might cause an exception
Except: Do this if these was an exception
Else: Do this if there were no exceptions
Finally: Do this no matter what happens
"""

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")  # file does not exist error
    a_dictionary = {"key": "value"}
    print(a_dictionary["adsfajds"])
except FileNotFoundError:
    print("There was an error")
    file = open("a_file.txt", "w")  # so the best next option is to create it
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

# # you can even raise an Error using 'raise' so the error show no matter what happens
# finally:
#     raise TypeError("This is the error I made up")
"""
The 'raise' error can be useful for example if a user stated their height as 300cm 
This would be unrealistic number although there are no computational error. 
So we can prompt the user saying, "hey!, there might be an error with this person's height etc"

if height > 300:
    raise ValueError
"""

# Challenge 1
"""
We've got some buggy code. Try running the code. The code will crash and give you an IndexError. 
This is because we're looking through the list of fruits for an index that is out of range.

Use what you've learnt about exception handling to prevent the program from crashing. 
If the user enters something that is out of range just print a default output of "Fruit pie".
INPUT:
["Apple", "Pear", "Orange"]

fruits = eval(input())
# Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
    print(fruit + " pie")
  except IndexError:
    print("Fruit pie")

# Do not change the code below
make_pie(4)

OUTPUT:
Fruit pie
"""
# Challenge 2
"""
"We've got some buggy code, try running the code. The code will crash and give you a KeyError. This is because some of the posts in the facebook_posts don't have any "Likes".

Objective
Use what you've learnt about exception handling to prevent the program from crashing.

Example Input
[{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
Using the eval() function we can create a list of dictionaries that looks like this:

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]"
"""
# Input
[{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3},
 {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass


print(total_likes)