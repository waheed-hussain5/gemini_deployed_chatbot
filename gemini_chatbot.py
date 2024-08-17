import streamlit as st
import google.generativeai as genai

# Set up your Google Generative AI API key
# Replace with your actual API key

api_key= st.secrets.gemini_api  # this is used for streamlit, where i store the api
                                # in secrets of streamlit, can accessed like st.secrets.name
genai.configure(api_key=api_key)

# Initialize the Generative Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to get the response from the model
def get_response(prompt):
    response = model.generate_content([prompt])
    return response.text

# Streamlit app layout
def main():
    #st.set_page_config(page_title="Google gemini 1.5-flash Chatbot", page_icon=":robot:")
    #st.set_page_config(page_title="Chatbot by Waheed", page_icon= "🤖")

    st.markdown("<h1 style='text-align: center; color: blue;'>Gen-AI Chatbot by Waheed...</h1>", unsafe_allow_html=True)
    st.title("Model: Google gemini 1.5-flash")
    # CSS styling
    st.markdown("""
        <style>
        body {
            background-color: #2C2C2C;
            color: #FFFFFF;
        }
        .chat-container {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px #000;
        }
        .input-container {
            background-color: #3B3B3B;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 0px 5px #000;
        }
        .input-box {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            color: #FFFFFF;
            background-color: #555555;
        }
        .submit-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            margin-top: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .submit-button:hover {
            background-color: #45a049;
        }
        .response-box {
            margin-top: 20px;
            padding: 10px;
            background-color: #3B3B3B;
            border-radius: 10px;
            box-shadow: 0px 0px 5px #000;
        }
        </style>
    """, unsafe_allow_html=True)

    # Chatbot UI
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    
    user_input = st.text_input("Ask the chatbot:", key="input", placeholder="Type your question here...", label_visibility="hidden")
    
    #if st.button("➔", key="submit", help="Click to get a response from the chatbot", use_container_width=False):
        #user_input = st.session_state.input  # 
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Send", key="submit", help="Click to get a response from the chatbot", use_container_width=True):
        user_input = st.session_state.input  

        if user_input:
            response = get_response(user_input)
            st.markdown("<div class='response-box'>", unsafe_allow_html=True)
            st.markdown(f"**You:** {user_input}", unsafe_allow_html=True)
            st.markdown(f"**Bot:** \n{response}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
