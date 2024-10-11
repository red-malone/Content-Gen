from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
api_key = os.getenv("API_KEY")
os.environ["HUGGINGFACE_HUB_TYPE"] = api_key
id = "meta-llama/Llama-3.2-3B-Instruct"

# Initialize HuggingFace LLM with repo_id and API key
llm = HuggingFaceEndpoint(repo_id=id, temperature=0.6, huggingfacehub_api_token=api_key,max_new_tokens=700)

# Create a PromptTemplate
template = PromptTemplate(
    input_variables=["topic", "blog_title"],
    template="Write a blog post about {topic}. The blog should be informative, engaging, and provide useful insights. Title: {blog_title}\n\nContent:"
)

def lang(topic,blog_title):
    chain = template | llm | StrOutputParser()
    return chain.invoke({"topic": topic, "blog_title": blog_title})


result = lang("The Importance of Coffee in Productivity", "How Coffee Fuels Productivity in the Modern Workplace")
print(result)
