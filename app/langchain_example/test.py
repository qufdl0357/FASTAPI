from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

import os 

os.environ["OPENAI_API_KEY"] = "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"
os.environ["APIFY_API_TOKEN"] = "apify_api_6ICdRCacZp3sonbNYPWhVzNv7DxBCx2r2r8c"
os.environ["GOOGLE_API_KEY"] = "AIzaSyC_GULKOkPFTFTI3GqSbd6v1U07LUJ4Ook"
os.environ["GOOGLE_CSE_ID"] = "334c6e9dd68da48e6"

def llminvoke(input):
	llm = OpenAI()
	chat_model = ChatOpenAI()
	messages = [HumanMessage(content = input)]
	output1 = llm.invoke(input)
	output2 = chat_model.invoke(messages)

	return output1, output2

if __name__ == "__main__":
	output = llminvoke("hello world")
	print(type(output))
	print(output)
	
    