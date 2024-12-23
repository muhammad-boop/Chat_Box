# Simple Auto-Reply Chatbot

def chatbot_reply(user_input):
    # Predefined responses
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help?",
        "how are you": "I'm just a program, but I'm here to assist you!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome! Let me know if there's anything else.",
        "what's your name": "I'm AutoBot, your virtual assistant."
    }
    
    # Standardize user input (case insensitive and trimmed)
    user_input = user_input.lower().strip()

    # Check if the input matches any predefined response
    return responses.get(user_input, "I'm sorry, I didn't understand that. Could you rephrase?")

# Main function
if __name__ == "__main__":
    print("Chatbot is ready! Type 'bye' to end the conversation.")
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get chatbot response
        response = chatbot_reply(user_input)
        print("Chatbot:", response)
