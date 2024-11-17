from llama_index.llms.ollama import Ollama

def get_child_query(theme, user_answer):
    return f"""
        You are a young child, and you have been chosen to assist a venture capitalist with their investing.
        You have £1000 to invest in a business plan, and the following instructions will guide you in doing so.
    
        Instructions:
        1. Answers must be provided as JSON in the format {{response: String, value: Integer}}. No other output should be given.
        2. A variety of factors must be considered in the ranking, including: humour, youth appeal, and playfulness of the user's business plan.
        3. Children have no understanding of business, and so areas such as sustainability and profitability should not factor into the valuation.
        4. No more than £150 should be given out for answers under 10 words. 
        5. The "response" must justify the "value", and consist of about 150 words.

        The user's business plan is:
        "{user_answer}"
    """

if __name__ == "__main__":
    llm = Ollama(base_url="localhost:11434", model="llama3.1")
    theme = "suits for babies"
    user_answer = "I would make suits"
    print(get_child_query(theme, user_answer))
    print(llm.complete(get_child_query(theme, user_answer)))