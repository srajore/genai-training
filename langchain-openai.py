
#from  langchain.llms import OpenAI  (Still code is working with warnings)

#from langchain_community.llms import OpenAI

from langchain_openai import OpenAI


llm = OpenAI(openai_api_key="",model_name="gpt-3.5-turbo-instruct")


prompt= "What is GenAI ,explain in simple term?"

#print(llm.predict(prompt))

print(llm.invoke(prompt))


