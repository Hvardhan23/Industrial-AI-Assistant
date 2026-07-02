import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

#from langchain.chains.combine_documents import create_stuff_documents_chain
#from langchain.chains import create_retrieval_chain

load_dotenv()

def get_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

    return llm

#llm cant understnad document object need to convert into plain text
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

#ask
def ask_question(question, retriever):

    docs = retriever.invoke(question)

    context = format_docs(docs)

    prompt = f"""
        You are an Industrial AI Maintenance Assistant.

        Answer ONLY using the context.

        If the answer is unavailable, reply:

        'I could not find that information in the maintenance manual.'

        Context:
        {context}

        Question:
        {question}
        """

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content