#Langchain>Modules>Retrieval>Retrievers>MultiQueryRetriever
#https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector
def _Modules_MultiQueryRetriever(human_input="what is this about"):

  # Build a sample vectorDB
  from langchain.document_loaders import WebBaseLoader
  from langchain.embeddings.openai import OpenAIEmbeddings
  from langchain.text_splitter import RecursiveCharacterTextSplitter
  from langchain.vectorstores import Chroma
  from langchain.chat_models import ChatOpenAI
  from langchain.retrievers.multi_query import MultiQueryRetriever

  # Load blog post
  loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
  data = loader.load()

  # Split
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
  splits = text_splitter.split_documents(data)

  # VectorDB
  embedding = OpenAIEmbeddings()
  vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

  llm = ChatOpenAI(temperature=0)
  retriever_from_llm = MultiQueryRetriever.from_llm(
      retriever=vectordb.as_retriever(), llm=llm
  )

  # Set logging for the queries
  import logging

  logging.basicConfig()
  logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

  unique_docs = retriever_from_llm.get_relevant_documents(query=human_input)

  from langchain import hub

  rag_prompt = hub.pull("rlm/rag-prompt")
  print(rag_prompt)

  # RAG chain 생성
  from langchain.schema.runnable import RunnablePassthrough

  # pipe operator를 활용한 체인 생성
  rag_chain = (
      {"context": retriever_from_llm, "question": RunnablePassthrough()}
      | rag_prompt
      | llm
  )

  output = rag_chain.invoke("what is chain of thought?")
  return output

#Langchain>Modules>Retrieval>Retrievers>EnsembleRetriever
#https://python.langchain.com/docs/modules/data_connection/retrievers/ensemble
def _Modules_EnsembleRetriever(human_input="what is this about"):
  pass

#Langchain>Modules>Retrieval>Retrievers>MultiVectorRetriever
#https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector
def _Modules_MultiVectorRetriever(human_input="what is this about"):
  pass

#Langchain>Modules>Retrieval>Retrievers>ParentDocumentRetriever
#https://python.langchain.com/docs/modules/data_connection/retrievers/parent_document_retriever
def _Modules_ParentDocumentRetriever(human_input="what is this about"):
  pass

#Langchain>Modules>Retrieval>Retrievers>SelfQueryRetriever
#https://python.langchain.com/docs/modules/data_connection/retrievers/self_query
def _Modules_SelfQueryRetriever(human_input="what is this about"):
  pass

#Langchain>Modules>Retrieval>Retrievers>WebResearchRetriever
#https://python.langchain.com/docs/modules/data_connection/retrievers/web_research
def _Modules_WebResearchRetriever(human_input="what is this about"):
  pass