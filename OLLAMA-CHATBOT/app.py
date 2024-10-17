#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import  StrOutputParser
from langchain_community.llms import Ollama 
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()



#Langsmit tracking

os.environ["LANGCHAIN_TRACING_V2"]="true"
#os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_PROJECT"] = f"OLLAMA Project"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#Prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please respond to user queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain demo with OLLAMA")

input_text=st.text_input("search the topic you want")

#OPEN AI LLM

llm=Ollama(model="llama3")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))