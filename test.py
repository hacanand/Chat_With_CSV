# import os
# from fastapi import FastAPI, Request
# from dotenv import load_dotenv
# from langchain_experimental.agents.agent_toolkits import create_csv_agent
# from langchain_community.chat_models import ChatOpenAI
# load_dotenv();

# app = FastAPI()
# @app.get("/chat_with_csv")
# async def chat_with_csv(request: Request):
#         text_data=await request.json()
#         query=text_data.get('query')
#         llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key = os.environ["OPENAI_API_KEY"])
#         agent_executer=create_csv_agent(llm, 'salaries.csv', verbose=True)
#         response = agent_executer.invoke(query)
#         return response
     