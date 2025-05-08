from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate



class LLMService:
    def __init__(self,model='mistral'):
        self.ollama = ChatOllama(model=model)

    def query(self, prompt: str,context = None):
        if context:
            promptTemp = PromptTemplate(input_variables=["input", "context"], template="Answer the following prompt: {input} using the following context only: {context}")
            formatted_prompt = promptTemp.format(input=prompt, context=context)
        else:
            promptTemp = PromptTemplate(input_variables=["input"], template="Answer the following prompot: {input}")
            formatted_prompt = promptTemp.format(input=prompt)

        for chunk in self.ollama.stream(formatted_prompt):
            if chunk.text:
                print(chunk.text, end="", flush=True)
                yield chunk.text
   