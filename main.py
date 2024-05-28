import os
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
# from langchain import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
def llm_response(query):
    # llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key= os.environ["OPENAI_API_KEY"])
    llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",google_api_key=os.environ["GOOGLE_API_KEY"],temperature=0.5)
    agent_executer=create_csv_agent(llm, 'salaries.csv', verbose=True,return_intermediate_steps=True)
    response = agent_executer.invoke(query)
    return response
          


def ChatWithCsvGui():
        st.title('Chat With CSV')
        st.write('This is a chat interface that uses a given CSV file as a knowledge base.')
        user_question = st.text_input('Ask a question about the CSV file:')
        if st.button('Submit'):
            if not user_question:
                st.warning('Please input a valid text.')
                st.stop()
            else:
                res=llm_response(user_question)
                st.write(res['output'])
                st.write('Intermediate Steps For better Understanding:')
                st.write(res[intermediate_steps])

ChatWithCsvGui()