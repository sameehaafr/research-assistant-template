# Building web application components
import streamlit as st

# Making HTTP requests
import requests

# Pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# Reading and manipulating PDF files
import PyPDF2

# Interact with the operating system 
import os

# Imports key from module
from apikey import apikey

# Natural language processing tasks/building chatbot related
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI


# Accesses the environment variables in the operating system with apikey as credentials
os.environ['OPENAI_API_KEY'] = apikey

def main():
    # Insert title
    ...
    # Insert file uploader
    ...
    # Insert text input prompt
    ...
    # Initialize history storage
    ...
    # Scrape content from uploaded pdf file
    ...
    # Set up prompt template
    ...
    # Use ConversationBufferMemory allows for storing messages and then extracts the messages in a variable
    ...
    # Build LLM Chain using LangChain
    ...
    # Run prompt through chain
    ...

if __name__ == "__main__":
    main()