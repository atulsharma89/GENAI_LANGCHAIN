from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import  StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

#Langsmit tracking
LANGCHAIN_PROJECT="Tutorial"
os.environ["LANGCHAIN_TRACING_V2"]="true"
#os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_PROJECT"] = f"Tutorial-1"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#Prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please respond to user queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain demo with Open AI")

input_text=st.text_input("search the topic you want")

#OPEN AI LLM

llm=ChatOpenAI(model="gpt-3.5-turbo")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))