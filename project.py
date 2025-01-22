from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_ollama import ChatOllama
from langchain.prompts import *
import langserve
import fastapi
import uvicorn
from langserve import RemoteRunnable
from langchain_community.chat_message_histories import ChatMessageHistory

model = ChatOllama(model='qwen2.5:latest')
parser = StrOutputParser()

promt = ChatPromptTemplate([

    ('system', '你是一个助手，用{language}回答问题')
])



store = {}

chain = promt | model | parser



def get_session_history(sesssion_id:str):

    if sesssion_id not in store:
        store[sesssion_id] = ChatMessageHistory()
    return store[sesssion_id]

do_message = RunnableWithMessageHistory(

    chain,
    get_session_history,
    input_messages_key='my_msg'
)

config = {'configurable':{'session_id':'zs123'}}

#第一轮
resp = do_message.invoke(

    {

        'my_msg':[HumanMessage(content='你好我是森')],
        'language':'中文',

    },
    config

)

print(resp)

resp = do_message.invoke(

    {

        'my_msg': [HumanMessage(content='请问我的名字是什么')],
        'language': '中文',

    },
    config

)

print(resp)