# # Get user input
# def Madlibs():
name = input("Enter a name: ")
city = input("Enter a city: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")  # Fixed spelling

# Generate the story
story = f"Eik din, {name} {city} gaya. Wahan usne ek {adjective} {animal} dekha jo {verb} raha tha. Ye dekh kar, {name} bohot hairan hua!"
print(story)


