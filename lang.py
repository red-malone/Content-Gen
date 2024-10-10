from dotenv import load_dotenv
import os
from langchain import PromptTemplate, LLMChain
from langchain_huggingface import HuggingFaceEndpoint


load_dotenv()
api_key = os.getenv("API_KEY")
id="meta-llama/Llama-3.2-1B"
llm=HuggingFaceEndpoint(repo_id=id,temperature=0.7,token=api_key)
template=PromptTemplate(
        input_variables=["content"],
        template="Write {content} needed for the website",
    )

# llm = OpenAI(temperature=0.7, openai_api_key=api_key)
# def lang(content):

    
#     chain = LLMChain(llm=llm, prompt=template)

#     return chain.run(content)
    