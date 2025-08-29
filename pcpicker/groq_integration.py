import os
from groq import Groq
def check_compatibility_with_groq(components):
    # Initialize the Groq client with the provided API key
    client = Groq(api_key="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")

    # Construct the message prompt for compatibility check
    prompt = f" Here is the component list {components}. You need to check if each primary component is compatible with one another. If all the components are compatible, simply return 'everything is goods'. If there are any compatibility issues, summarize the problems concisely in bullet points, indicating which component has a conflict with which other component. Provide only the essential details of the issue in one or two sentences and provide only details of componets that r not comaptible and as a separate point genrate wehter it can run or not run like tht keyword too if it cannot run in the end of report mention 'cannot run'." 

    try:
        # Make an API call to Groq's chat completion model using the prompt
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",temperature=0.01  # Ensure the correct model is used
        )

        # Print the entire response to verify if it was successful
        print("Full API Response:", chat_completion)

        # Extract the first response from the model
        response = chat_completion.choices[0].message.content

        # Print the specific response being returned
        print("Model's Response:", response)

        return response

    except Exception as e:
        # Print any errors encountered during the API call
        print(f"Error occurred: {e}")
        return "Error: Unable to check compatibility at this time."

def query_classifier(user_query):
    client =Groq(api_key="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")

    path=r"C:\Users\pavit\programing\pcpickertool\table_schema.txt"
    
    with open(path, "r", encoding="utf-8") as f:

        table_definition = f.read()

    Prompt= f"""

    You are a smart intent classification assistant for a PC Builder Tool.

    Your task is to classify the **user query** as one of the following types:

    1. SQL — The query is asking for **data values** (e.g., comparisons, filters, rankings) from the PC components database.
    2. Website — The query is asking for **help, guidance, or explanation** about how the website or PC Picker tool works.

    You are also given the tables Defintion below. If the user's query mentions **any column or concept** from these tables, it's likely an SQL query.

    ---

    Table definition:
    {table_definition}

    ---

    ### Examples:

    Query: "Which CPU has the highest cpu_mark?"
    → Answer: SQL

    Query: "How do I save a build on this website?"
    → Answer: no

    Query: "Show me GPUs with G3mark < 2000"
    → Answer: SQL

    Query: "What does the summary page display?"
    → Answer: no

    Query: "Which RAM has the lowest CAS latency?"
    → Answer: SQL

    Query: "What is a CPU cooler and why is it needed?"
    → Answer: no

    ---

    Now classify this user query below.

    User Query:
    {user_query}

    Return only one word: SQL or no

    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": Prompt}],
            model="meta-llama/llama-4-scout-17b-16e-instruct",temperature=0.01  # Ensure the correct model is used
        )

        # Print the entire response to verify if it was successful
        print("Full API Response:", chat_completion)

        # Extract the first response from the model
        response = chat_completion.choices[0].message.content

        # Print the specific response being returned
        print("Model's Response:", response)

        return response
    except Exception as e:
        # Print any errors encountered during the API call
        print(f"Error occurred: {e}")
        return "Error: Unable to check Query"


