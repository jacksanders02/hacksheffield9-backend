from llama_index.llms.ollama import Ollama
import personalities

# Setup model
llm = Ollama(base_url="localhost:11434", model="gemma2")

def get_all_queries(theme, user_answer):
  agent1 = llm.complete(personalities.get_business_expert_query(theme, user_answer))
  agent2 = llm.complete(personalities.get_random_bloke_query(theme, user_answer))
  agent3 = llm.complete(personalities.get_sustainability_query(theme, user_answer))
  agent4 = llm.complete(personalities.get_child_query(theme, user_answer))
