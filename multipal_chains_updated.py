from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv(".env", override=True)

llm = OpenAI()

# Template for generating the outline
template1 = """
    write a blog outline given a topic

    Topic: {topic}
"""

prompt_template1 = PromptTemplate(input_variables=["topic"], template=template1)

# Template for generating the article based on the outline
template2 = """
    write a blog article based on below outline

    Outline: {outline}
"""

prompt_template2 = PromptTemplate(input_variables=["outline"], template=template2)

# Create the outline chain
outline_chain = LLMChain(llm=llm, prompt=prompt_template1, output_key="outline")

# Create the article chain
artical_chain = LLMChain(llm=llm, prompt=prompt_template2, output_key="artical")

# Combine both chains into a final sequential chain
overall_chain = SequentialChain(
    chains=[outline_chain, artical_chain],
    input_variables=["topic"],
    output_variables=["outline", "artical"],
    verbose=True
)

# Use invoke to execute the overall chain
response = overall_chain.invoke({ "topic": "Generative AI" })

print(response)
