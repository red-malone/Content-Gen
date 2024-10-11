from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
api_key = os.getenv("API_KEY")
os.environ["HUGGINGFACE_HUB_TYPE"] = api_key
id = "meta-llama/Llama-3.2-1B"

# Initialize HuggingFace LLM with repo_id and API key
llm = HuggingFaceEndpoint(repo_id=id, temperature=0.7, huggingfacehub_api_token=api_key)

# Create a PromptTemplate
template = PromptTemplate(
    input_variables=["content"],
    template="Provide contents to be written in this {content} themed website. Comma separate the steps",
)

def lang(content):
    # Create a sequence where the template feeds into the LLM
    chain = template | llm | StrOutputParser()
    return chain.invoke(content)

# Example usage
result = lang("batman")
print(result)
