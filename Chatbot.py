import re

def chatbot_response(user_input):
    # Convert user input to lower case to make the bot case insensitive
    user_input = user_input.lower()

    # Define responses
    if re.search(r'\b(capital of france)\b', user_input):
        return "The capital of France is Paris."
    elif re.search(r'\b(capital of germany)\b', user_input):
        return "The capital of Germany is Berlin."
    elif re.search(r'\b(capital of japan)\b', user_input):
        return "The capital of Japan is Tokyo."
    elif re.search(r'\b(largest ocean)\b', user_input):
        return "The largest ocean is the Pacific Ocean."
    elif re.search(r'\b(longest river)\b', user_input):
        return "The longest river in the world is the Nile River."
    elif re.search(r'\b(highest mountain)\b', user_input):
        return "The highest mountain in the world is Mount Everest."
    elif re.search(r'\b(chemical symbol for water)\b', user_input):
        return "The chemical symbol for water is H2O."
    else:
        # Default response for unknown queries
        return "I'm sorry, I don't have the answer to that question. Can you please ask something else?"

# Main loop to keep the chatbot running
def main():
    print("ChatBot: Hello! You can ask me general knowledge questions. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
