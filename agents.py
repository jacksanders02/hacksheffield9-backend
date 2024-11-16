from llama_index.llms.ollama import Ollama
import personalities

# Setup model
llm = Ollama(base_url="localhost:11434", model="gemma2")

def get_all_queries(theme, user_answer):
  agent1 = llm.complete(personalities.get_business_expert_query(theme, user_answer))
  agent2 = llm.complete(personalities.get_random_bloke_query(theme, user_answer))
  agent3 = llm.complete(personalities.get_sustainability_inclusivity_query(theme, user_answer))
  agent4 = llm.complete(personalities.get_child_query(theme, user_answer))
  
  print('--------------------------------------------------------------------------------------------')
  print('---------------------------------Countess of Crookes----------------------------------------')
  print(agent1)
  print('--------------------------------------------------------------------------------------------')
  print('----------------------------------Brian From The Pub----------------------------------------')
  print(agent2)
  print('--------------------------------------------------------------------------------------------')
  print('----------------------------Sue Stainability and Ian Clusivity------------------------------')
  print(agent3)
  print('--------------------------------------------------------------------------------------------')
  print('----------------------------------------Tiny Tim--------------------------------------------')
  print(agent4)
  print('--------------------------------------------------------------------------------------------')
  print('--------------------------------------------------------------------------------------------')



theme = "bank accounts for polar bears"
answer = "Open a natwest branch in the arctic circle and use fish currency. I will charge high interest to make profits."

get_all_queries(theme, answer)