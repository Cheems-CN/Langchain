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
prompt = ChatPromptTemplate([

    ('system', 'you are a teacher teaching math'),
    ('ai', 'hello, whats your problem about this'),
    ('user', '{content}.Can you teach me some?')
])

chain = prompt| model | parser


app = fastapi.FastAPI(title='''sen's serve''', version='V1.0.0', description='miss u')
langserve.add_routes(

    app,
    chain,
    path="/senmissu"

)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
