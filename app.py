import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


# UI setup
st.title(" Simple GenAI Chatbot")


# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "Question: {question}")
])

# Load model
llm = OllamaLLM(model="gemma:2b")

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Input
user_input = st.text_input(" Ask something:")

# Run chatbot
if user_input:
    try:
        response = chain.invoke({
            "question": user_input
        })

        st.write(" Bot:", response)

    except Exception as e:
        st.error(f"Error: {e}")