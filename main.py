# This is a sample Python script.
from typing import cast

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#


from dotenv import load_dotenv
from langchain.chains.summarize.map_reduce_prompt import prompt_template

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

#temperature randomness ve creativity
model = ChatOpenAI(model="gpt-4",temperature=0.1);
#messages = [
 #   SystemMessage(content="Translate the following from English to Spanish"),
#  HumanMessage(content="Hi"),
#]

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),("user","{text}")
    ]
)

parser = StrOutputParser()
#response = model.invoke(messages)

chain = prompt_template | model | parser

app =  FastAPI(
    title="Translate into {language}",
    version="0.1.0",
    description="Translate into {language}",
)

add_routes(
    app,
    chain,
    path="/chain"
)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 #   response = model.invoke(messages)
 #   print(chain.invoke({"language":"Italian", "text":"Hi"}))
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
