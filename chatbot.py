def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    your_name = input()  # Read user input
    print(f"What a great name you have, {your_name}!")

# Now we can use these functions
greet("Twriters", 2025)
remind_name()
