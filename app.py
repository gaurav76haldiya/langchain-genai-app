import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title="Ollama GenAI App",
    page_icon="🤖"
)

st.title("🤖 LangChain + Ollama")
st.write("Ask a question and get an AI-generated response.")

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

llm = OllamaLLM(
    model="llama3.2:3b",
    base_url="https://YOUR-OLLAMA-SERVER"
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

question = st.text_input(
    "What question do you have in mind?",
    placeholder="Ask anything..."
)

if question:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({
                "question": question
            })

            st.subheader("Response")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")
