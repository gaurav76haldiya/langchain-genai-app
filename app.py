import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title="Ollama GenAI",
    page_icon="🤖"
)

st.title("🤖 LangChain + Ollama")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. "
        "Answer clearly and accurately."
    ),
    ("human", "{question}")
])

llm = OllamaLLM(
    model="llama3.2:3b",
    base_url="http://localhost:11434"
)

chain = prompt | llm | StrOutputParser()

question = st.text_input(
    "Ask a question",
    placeholder="What is Generative AI?"
)

if question:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"question": question})
            st.subheader("Response")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
