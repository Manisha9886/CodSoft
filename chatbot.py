# %%
import re

# %%
import re

def get_response(user_input):
    user_input = user_input.lower()
    patterns = {
        r'\b(hi|hello|hey)\b': "Hello! What can I help you with?",
        r'\b(hi|hello|hey)\b': "Hello! What can I help you with?",
        r'\b(good evening|good morning|good afternoon)\b': "Great day, how can I help you today?",
        r'\bhow are you\b': "I'm a virtual bot and have no feelings so I can't answer that question",
        r'\bwhat is your name\b': "I am a virtual bot basically called chatbot since that's what they call me!",
        r'\bwhere are you from\b': "I am from digital world!",
        r'\bcan you eat\b': "No, I can't eat but I can recommend you some delicious recipes of different food!Do you want me to recommend?",
        r'\b(what are your hobbies|hobby)\b': "My main hobby is to help you can ask me anything",
        r'\b(bye|goodbye|see you)\b': "Goodbye! Have a wonderful day!",
        r'\b(can you help me|i need help)\b': "Sure, tell me what happened?",
        r'\b(who created you|origin|who brought you into existence)\b': "I was created by Manisha.",
        r'\b(what is your name|who are you)\b': "I'm a simple chatbot made to help you!",
        r'\b(thank you|thanks)\b': "You're welcome!",
    }
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response
    return "I'm not sure I understand. Could you please make it clear?"
def chatbot():
    print(" Hieee! I am a chatbot. Nice to see you! Type 'exit' to quit.")
    print("`" * 80)
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'exit':
            print("Chatbot: Conversation over byeee.")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

chatbot()



