import os
from dotenv import load_dotenv
load_dotenv()


#load the GROQ and Open AI API key

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")


import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")


# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://en.wikipedia.org/wiki/Narendra_Modi",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)


docs = loader.load()

print(docs)




