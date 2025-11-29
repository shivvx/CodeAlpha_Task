import datetime  # Imported to show the current time

def get_bot_response(user_input):
    # Normalize input: make lowercase and remove extra spaces
    message = user_input.lower().strip()

    # --- Expanded Logic ---
    
    # 1. Greetings (checks if input is exactly one of these)
    if message in ["hello", "hi", "hey", "sup"]:
        return "Hello there! How can I help you today?"

    # 2. Well-being (checks if the phrase exists inside the message)
    elif "how are you" in message:
        return "I'm just a script, but I'm running bug-free! How are you?"

    # 3. Identity/Name
    elif "your name" in message or "who are you" in message:
        return "I am a Python Chatbot created by you."

    # 4. Jokes
    elif "joke" in message:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    # 5. Technology/Python
    elif "python" in message:
        return "I love Python! It's the language that gives me life."

    # 6. Current Time (Dynamic response)
    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current system time is {current_time}."

    # 7. Farewell
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    # 8. Default (Catch-all)
    else:
        return "I didn't quite catch that. Try asking for a joke, the time, or just say 'Hello'."

def main():
    print("--- Expanded Chatbot (Type 'bye' to exit) ---")

    while True:
        try:
            user_text = input("You: ")
            
            # Get the response
            response = get_bot_response(user_text)
            print(f"Bot: {response}")

            # Check if user wants to quit
            if user_text.lower().strip() in ["bye", "goodbye", "exit"]:
                break
                
        except KeyboardInterrupt:
            # Handles if you press Ctrl+C
            print("\nBot: Force closing... Goodbye!")
            break

if __name__ == "__main__":
    main()