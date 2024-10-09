from langchain_core.tools import tool

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

@tool
def multiply(first_int: int, second_int:int) -> int:

    """Multiply two integers together """

    return first_int * second_int


# Initilize the OpenAIChat model

llm= ChatOpenAI(

    temperature=0,
    model_name="gpt-4",
    max_tokens=4000,
    #openai_api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

)

# Bind the multiply tool to the OpenAIChat model

llm_with_tool = llm.bind_tools([multiply])

# Invoke the modle with a question

# message= llm_with_tool.invoke("what is 5 times 10")

#print(message)

#print(message.tool_calls)

chain= llm_with_tool | (lambda x: x.tool_calls[0]["args"]) | multiply

print(chain.invoke("what is 5 times 11 "))











