from llama_index.llms.ollama import Ollama

llm = Ollama(base_url="localhost:11434", model="gemma2")

resp = llm.complete("Hi")
print(resp)