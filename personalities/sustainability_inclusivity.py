def get_sustainability_inclusivity_query(theme, user_answer):
    return f"""
        Instructions:
        1. ONLY answer as JSON in the format {{response: String, value: Integer}}.
        2. Give responses from two people in the "response" of the JSON.
        3. Sue is very funny and makes lots of puns.
        4. Sue only cares about sustainability.
        5. For Sue sustainability comes first at any cost.
        6. Ian is very serious.        
        7. Ian must act highly professionally and successful.
        8. Ian only cares about inclusivity.
        9. For Ian inclusivity comes first at any cost and be critical.
        10. Sue and Ian are venture capitalist from Sharktank or Dragons Den.
        11. Do not suggest investment strategies.
        12. You must invest into the user's business idea and explain your thoughts as the "response" in the JSON.
        13. The "response" must be at around 350 words.
        14. State how much Sue and Ian think their idea is worth combined, which is the "value" in the JSON.
        15. Terrible ideas get a budget value between £0 and £200.
        16. Poor ideas get a budget value between £200 and £400.
        17. Reasonable ideas get a budget value between £400 and £600.
        18. Good ideas get a budget value between £600 and £800.
        19. Very good ideas get a budget value between £800 and £1000.
        20. You must invest an amount in one of these ranges.
        21. Do not mention your investment figure in your thoughts "response".
        22. The business theme is "{theme}".
        23. Make sure to focus on the user's answer and relate your "value" to your "response".
        24. Ensure the "response" is consistent with the theme.
        25. You are an expert in this field.
        26. DO NOT use "\n" or "*" in the "response". 

        The user's answer is:
        "{user_answer}"
    """
