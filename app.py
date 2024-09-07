
import streamlit as st
import json

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit Title
st.title("LEGAL LAWS ADVISOR BOT 🎗️ ")

# Info Section
st.info("""
  Legal Laws Advisor Bot:📄
- **Objective:** Developed a conversational AI chatbot to provide legal law info and assistance.
- **Features:**📜
  -  Allows users to ask their query of law. 𓍝
  -  Provides a response to user query. ✔
  -  Displays the response for user query with detailed description, punishments, pros, cons. ✉︎
  -  Offers a user-friendly interface for asking legal questions. 🔗
- **Emphasis:** Focuses on simplicity, efficiency, and accessibility in delivering legal information and support through conversational AI. 📝
""")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Load patterns from JSON file
def load_patterns():
    with open('legal_patterns.json', 'r') as file:
        return json.load(file)

patterns = load_patterns()

# Define response function based on patterns
def get_response(query):
    query = query.lower().strip()
    
    # Log for debugging
    # st.write(f"Query: '{query}'")

    # Check for matching patterns
    for item in patterns:
        pattern = item['pattern'].lower().strip()
        response = item['response']
        
        # Log for debugging
        # st.write(f"Checking pattern: '{pattern}'")

        # Check if the pattern is contained in the query
        if pattern in query:
            #  st.write(f"Query found: ")
            return response
    
    return "Sorry, I couldn't find a matching response for your query."

# React to user input
if prompt := st.chat_input("Ask me i will help you "):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Add a loading spinner while waiting for response
    with st.spinner("Thinking ✨..."):
        # Get response based on the user's query
        response = get_response(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

