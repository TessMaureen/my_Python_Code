def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")
    print("I am here to assist you with academic writing, research, and study tips!")

def remind_name():
    print("Please, remind me your name.")
    your_name = input()  # Read user input
    print(f"What a great name you have, {your_name}!")

def offer_help():
    print("How can I assist you today?")
    print("I can help with:")
    print("1. Writing essays and research papers")
    print("2. Formatting and citations")
    print("3. Finding reliable sources")
    print("4. Study tips and time management")

# Now we can use these functions
greet("Twriters", 2025)
remind_name()
offer_help()
