# Building web application components
import streamlit as st

# Making HTTP requests
import requests

# Pulling data out of HTML and XML files
from bs4 import BeautifulSoup

# Reading and manipulating PDF files
import PyPDF2

# Natural language processing tasks/building chatbot related
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI

# Make sidebar to insert OpenAI API key
openai_api_key = ...

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

# Method for scraping text from pdf files given an uploaded file
def pdf_scrape(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            return text
        else:
            return "Uploaded file is not a PDF."
    except Exception as e:
        print(e)
        return f"Failed to retrieve text from the PDF: {e}"

# Method for scraping text from articles/blogs given a link
def web_scrape(url: str):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text(separator=" ", strip=True)
            return page_text
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"

if __name__ == "__main__":
    main()