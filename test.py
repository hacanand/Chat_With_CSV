import os
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
 
from langchain_community.chat_models import ChatOpenAI
load_dotenv()
def llm_response(query):
    llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key= os.environ["OPENAI_API_KEY"])
    agent_executer=create_csv_agent(llm, 'salaries.csv', verbose=True)
    response = agent_executer.invoke(query)
    return response
          


def ChatWithCsvGui():
        st.title('Chat With CSV')
        st.write('This is a chat interface that uses a given CSV file as a knowledge base.')
        user_question = st.text_input('Ask a question about the CSV file:')
        if st.button('Submit'):
            res=llm_response(user_question)
            st.write(res['output'])



ChatWithCsvGui()