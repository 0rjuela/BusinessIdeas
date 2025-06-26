from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

from langchain.globals import set_debug
set_debug(True)
from langchain.globals import set_verbose
set_verbose(True)

load_dotenv()

# Add this line to check if the API key is loaded
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    print("OpenAI API key loaded successfully.")
else:
    print("ERROR: OpenAI API key not found. Please check your .env file.")
    exit()

def business_ideas(industry, audience):
    try:
        llm = OpenAI(temperature=0.5, request_timeout=30)
        output_parser = StrOutputParser()

        prompt_template = PromptTemplate(
            input_variables=['industry','audience'],
            template="""
            I want to start a business in the {industry}, I want to have this adapted
            to {audience}. Suggest me five profitable business ideas
            """     
        )
        
        # Create the chain using the pipe operator
        chain = prompt_template | llm | output_parser

        # Invoke the chain with the industry parameter
        idea = chain.invoke({"industry": industry, 'audience': audience })
        return idea
        
    except Exception as e:
        print(f"An error occurred during the OpenAI call: {e}")
        return "Error generating ideas."

if __name__ == "__main__":  
    print("Generating business ideas...")
    # Now you can specify different industries
    result = business_ideas("fintech", "latin american young pepole, from 20 o 30 years old")  
    print("Generated ideas:")
    print(result)