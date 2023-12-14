#LangChain/Get started/Quickstart

#LLM / Chat Model
#LLM: underlying model takes a string as input and returns a string
#ChatModel: underlying model takes a list of messages as input and returns a message
#name : llmInvoke
#desc : Invoke LLM
#link : https://python.langchain.com/docs/get_started/quickstart
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
def llminvoke(input):
	llm = OpenAI()
	chat_model = ChatOpenAI()
	messages = [HumanMessage(content = input)]
	output1 = llm.invoke(input)
	output2 = chat_model.invoke(messages)

	return output1, output2

#Prompt templates
#name : llmPromptTemplates
#desc : Prompt Templates for LLM
#link : https://python.langchain.com/docs/get_started/quickstart
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain
def llmPromptTemplates(product, human_text, llm):
	#PromptTemplates
	prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
	prompt.format(product = product)
	
	llm_prompt_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

	#Chat PromptTemplates
	template = "You are a helpful assistant that search information about {product}."
	human_template = "{text}"
	chat_prompt = ChatPromptTemplate.from_messages([
		("system", template),
		("human", human_template)
	])
	chat_prompt.format_messages(product = product, text = human_text)

	#Predict Answer
	output = ""

	return output
