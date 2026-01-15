import os 
from dotenv import load_dotenv
from langchain_perplexity import ChatPerplexity


load_dotenv()
PPLX_API_KEY=os.getenv("PPLX_API_KEY")
llm=ChatPerplexity(api_key=PPLX_API_KEY,model="sonar")