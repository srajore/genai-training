
from langchain_openai import OpenAI

from langchain.prompts import PromptTemplate

from langchain.chains import LLMChain,SequentialChain


from dotenv import load_dotenv

load_dotenv(".env",override=True)

llm=OpenAI()

template1= """
    write a blog outline given a topic

    Topic: {topic}

"""

prompt_template1=PromptTemplate(input_variables=["topic"],template=template1)


outline_chain=LLMChain(llm=llm,prompt=prompt_template1,output_key="outline")

template2= """
    write a blog artical  based on below  outline

    Outline: {outline}

"""

prompt_template2=PromptTemplate(input_variables=["outline"],template=template2)

artical_chain=LLMChain(llm=llm,prompt=prompt_template2,output_key="artical")

overall_chain=SequentialChain(
    chains=[outline_chain,artical_chain],
    input_variables=["topic"],
    output_variables=["outline","artical"],
    verbose=True

)

# Updated line to use invoke instead of __call__
response = overall_chain.invoke({ "topic": "Generative AI" })

print(response)



