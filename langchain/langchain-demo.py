
from langchain_community.llms import Ollama

if __name__ == "__main__":
    llm_model = Ollama(model="llama3")
    while True:
        prompt=input("You: ")
        response=llm_model.invoke(prompt)
        print(f"Bob: {response}")
