from llama_index.llms.ollama import Ollama
import personalities

PERSON_TO_AGENT = {
    "countess": personalities.get_business_expert_query,
    "dave": personalities.get_random_bloke_query,
    "sue": personalities.get_sustainability_inclusivity_query,
    "child": personalities.get_child_query
}

# Setup model
llm = Ollama(base_url="localhost:11434", model="gemma2")

def get_all_queries(theme, user_answer):
  agent1 = llm.complete(personalities.get_business_expert_query(theme, user_answer))
  agent2 = llm.complete(personalities.get_random_bloke_query(theme, user_answer))
  agent3 = llm.complete(personalities.get_sustainability_inclusivity_query(theme, user_answer))
  agent4 = llm.complete(personalities.get_child_query(theme, user_answer))

  print('############################################################################################')
  print('---------------------------------------- Theme ---------------------------------------------')
  print(theme)
  print('-------------------------------------- User Answer -----------------------------------------')
  print(user_answer)
  print('---------------------------------- Countess of Crookes -------------------------------------')
  print(agent1)
  print('----------------------------------- Dave From The Pub --------------------------------------')
  print(agent2)

  print('------------------------ Sue Stainability (Sister of Ian Clusivity) ------------------------')
  print(agent3)

  print('--------------------------------------- Tiny Tim -------------------------------------------')
  print(agent4)
  print('############################################################################################')

def main():
  while True:
    input_theme = input("Theme: ")
    if input_theme.lower() == "quit":
      break 
    user_answer = input("Answer: ")
    if user_answer.lower() == "quit":
      break
    get_all_queries(input_theme, user_answer)

def get_response(person: str, theme: str, answer: str):
    query_fun = PERSON_TO_AGENT[person.lower()]
    return llm.complete(query_fun(theme, answer))
