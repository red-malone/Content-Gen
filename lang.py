from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

load_dotenv()
api_key = os.getenv("API_KEY")
llm = OpenAI(temperature=0.7, openai_api_key=api_key)
def lang(content):

    template=PromptTemplate(
        input_variables=["content"],
        template="Write {content} needed for the website",
    )

    chain = LLMChain(llm=llm, prompt=template)

    return chain.run(content)
    