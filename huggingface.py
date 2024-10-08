
from langchain_community.llms import huggingface_hub


llm_huggingface =  huggingface_hub.HuggingFaceHub(

    repo_id="google/flan-t5-large",

    model_kwargs={ "temperature": 0, "max_length":64 } ,

    huggingfacehub_api_token=""

)

output=llm_huggingface.invoke("write a poem on artificial-intelligence")

print(output)



