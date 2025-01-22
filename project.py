from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.prompts import *
import langserve
import fastapi
import uvicorn
from langserve import RemoteRunnable
import  langchain_community

model = ChatOllama(model='qwen2.5:latest')
parser = StrOutputParser()




p = PromptTemplate(
    input_variables=['target'],
    template='你好，介绍一下{target}'
)
chain = p| model | parser
print(chain.invoke({'target':'自己'}))


