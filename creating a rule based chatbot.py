def chatbot_response(user_input):
    user_input = user_input.lower()
    if "what is python" in user_input:
        return "Python is a popular high-level, interpreted programming language known for its readability."
    elif "who created python" in user_input:
        return "Python was created by Guido van Rossum and first released in 1991."
    elif "what is a list" in user_input:
        return "A list in Python is a collection data type that is ordered and mutable. Lists are written with square brackets."
    elif "how to define a function" in user_input:
        return "You can define a function in Python using the 'def' keyword, followed by the function name and parentheses."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Feel free to ask more about Python anytime."
    else:
        return "I'm sorry, I can only answer questions about Python programming. Please ask something related to Python."

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        # No additional code is needed here. The chatbot loop already ends when "bye" or "exit" is detected.

        break
# The chatbot will continue to run until the user types "bye" or "exit".