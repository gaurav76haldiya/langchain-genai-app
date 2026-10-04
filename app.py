import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# -----------------------------
# Streamlit configuration
# -----------------------------

st.set_page_config(
    page_title="LangChain GenAI App",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LangChain GenAI App")
st.write("Ask a question and get an AI-generated response.")


# -----------------------------
# Get API key from Streamlit
# Secrets
# -----------------------------

groq_api_key = st.secrets["GROQ_API_KEY"]


# -----------------------------
# Prompt
# -----------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. "
        "Answer the user's question clearly and accurately."
    ),
    (
        "human",
        "{question}"
    )
])


# -----------------------------
# LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# -----------------------------
# Output parser
# -----------------------------

output_parser = StrOutputParser()


# -----------------------------
# LangChain
# -----------------------------

chain = prompt | llm | output_parser


# -----------------------------
# User input
# -----------------------------

question = st.text_input(
    "What question do you have in mind?",
    placeholder="Ask anything..."
)


# -----------------------------
# Generate response
# -----------------------------

if question:

    with st.spinner("Generating response..."):

        try:
            response = chain.invoke({
                "question": question
            })

            st.subheader("Response")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {str(e)}")
