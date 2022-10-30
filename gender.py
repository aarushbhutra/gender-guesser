import requests

#Get the user input of their name
name = input("Enter your name: ")
#Send a request to https://api.genderize.io/?name=your_name and replace your_name with name and and store the response in a variable called response
response = requests.get("https://api.genderize.io/?name=" + name)
#parse the response as JSON and store it in a variable called data
data = response.json()
#Print the value called gender
gender = data['gender']
probability = data['probability']
#Capitalize the first letter of gender and print it
print("You have a " + str(probability * 100) + "% chance of being a " + gender.capitalize() + "!")
