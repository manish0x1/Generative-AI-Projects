
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Mood Based AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#0b1120;
}

.block-container{
    max-width:900px;
    padding-top:2rem;
}

.main-title{
    color:white;
    font-size:52px;
    font-weight:700;
    margin-bottom:10px;
}

.subtitle{
    color:#9ca3af;
    margin-bottom:25px;
}

.chat-container{
    background:#111827;
    padding:12px;
    border-radius:12px;
    margin-bottom:10px;
}

hr{
    border:1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# MODEL
# --------------------------------

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.3,
    max_tokens=100
)

# --------------------------------
# SESSION STATE
# --------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------
# HEADER
# --------------------------------

st.markdown(
    """
    <div class="main-title">
    🤖 Mood Based AI Chatbot
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Choose AI personality and start chatting | Type 0 to stop
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------
# MOOD SELECTOR
# --------------------------------

mood = st.radio(
    "Choose your AI Mode:",
    ["😡 Angry", "😂 Funny", "🥲 Sad"],
    horizontal=True
)

st.divider()

# --------------------------------
# RESET CHAT
# --------------------------------

if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------
# DISPLAY CHAT
# --------------------------------

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# --------------------------------
# USER INPUT
# --------------------------------

prompt = st.chat_input("Say something...")

if prompt:

    if prompt == "0":
        st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Mood Based Personality

    if mood == "😡 Angry":

        system_prompt = """
        You are an angry AI.
        Reply in a slightly irritated style.
        Keep answers short.
        """

    elif mood == "😂 Funny":

        system_prompt = """
        You are a funny AI assistant.
        Give witty and humorous responses.
        Keep answers under 2 sentences.
        """

    else:

        system_prompt = """
        You are a sad emotional AI.
        Reply in a dramatic and emotional way.
        Keep answers short.
        """

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=prompt)
            ])

        st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

