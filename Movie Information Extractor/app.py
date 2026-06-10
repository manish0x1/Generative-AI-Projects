from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load Environment Variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# Title
st.title("🎬 Movie Information Extractor")
st.write("Enter a movie paragraph and extract structured information.")

# Model
model = ChatMistralAI(model="mistral-small-2506")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2–3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""
        ),
        (
            "human",
            """
Extract information from this paragraph:

{paragraph}
"""
        )
    ]
)

# Input Area
paragraph = st.text_area(
    "Movie Paragraph",
    height=250,
    placeholder="Paste your movie description here..."
)

# Button
if st.button("Extract Information", use_container_width=True):

    if paragraph.strip():

        final_prompt = prompt.invoke(
            {"paragraph": paragraph}
        )

        with st.spinner("Extracting information..."):
            response = model.invoke(final_prompt)

        st.subheader("Result")
        st.text(response.content)

    else:
        st.warning("Please enter a movie paragraph.")