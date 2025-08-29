from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from pcpicker.groq_integration import query_classifier
import ollama
import sqlite3
import pandas as pd

# Load the same model used during vector creation
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
components_db= FAISS.load_local("pc_componet_vector_store", embeddings=embedding_model, allow_dangerous_deserialization=True)
website_db = FAISS.load_local("pc_website_vector_store", embeddings=embedding_model, allow_dangerous_deserialization=True)


# from pcpicker.models import SaveBuild  

# def get_user_build_context(user_id):
#     try:
#         build = SaveBuild.objects.filter(user_id=user_id).latest("id")
        
#         return f"""
#         Build Name: {build.build_name}
#         CPU: {build.selected_cpu}
#         GPU: {build.selected_gpu}
#         Motherboard: {build.selected_motherboard}
#         RAM: {build.selected_ram}
#         Storage: {build.selected_storage}
#         Case: {build.selected_case}
#         PSU: {build.selected_psu}
#         OS: {build.selected_os}
#         CPU Cooler: {build.selected_cpu_cooler}
#         Monitor: {build.selected_monitor}
#         """
#     except SaveBuild.DoesNotExist:
#         return "No build found for this user."
def select_vector_db(user_query:str):
    Classified_answer = query_classifier(user_query)
    if "SQL" in Classified_answer :
        print("[INFO] Using components_Vector DB")
        type='SQL'
        return components_db, type
      
    
    elif "no" in Classified_answer:
        print("[INFO] Using website_Vector DB")
        type='webiste'
        return website_db, type

def hybrid_method(query: str):
    
    selected_db, type = select_vector_db(query)
    if type=="webiste":
         results = selected_db.similarity_search(query, k=5)
         context = "\n".join([doc.page_content for doc in results])
         return context,type
         
    elif type=="SQL":
        with open("table_schema.txt", "r") as file:
            table_schema = file.read()
    
        sql_query = get_sql_query(query,table_schema)    
        context= query_answer(sql_query)
        return context,type
         

def get_sql_query (query : str, table_schema):
    sql_prompt=f""" 
    You are a SQLite3 query generation assistant for a PC-building tool.

    Your job is to write correct and executable SQL queries specifically for SQLite, based on the user’s question and the given database schema.

    The table schema is provided below and includes the exact table names and column names. Use this schema to generate accurate queries.

    ---

    Rules:
    - Use only the exact column and table names from the schema.
    - Do not hallucinate or assume relationships unless clearly implied or evident by shared columns.
    - Never invent columns that are not present in the schema.
    - If the question can be answered from a single table, generate only one query.
    - Always use LIMIT when sorting to find the "highest", "lowest", or "top" results.
    - Match approximate terms in the user's question to the correct column names from the schema (e.g., "performance" might mean cpu_mark, etc.).

    ---

    Here is the available table schema:
    {table_schema}

    ---

    Examples:

    Q: Which CPU has the highest cpu_mark?  
    A:
    SELECT name, cpu_mark FROM pcpicker_cpu ORDER BY cpu_mark DESC LIMIT 1;

    Q: List all GPUs with G3mark greater than 5000  
    A:
    SELECT name, G3mark FROM pcpicker_gpu WHERE G3mark > 5000;

    Q: Show all RAM modules with CAS latency less than 16  
    A:
    SELECT name, cas_latency FROM pcpicker_ram WHERE cas_latency < 16;

    Q: Find CPU coolers with noise level under 30 dBA  
    A:
    SELECT name, noise_level FROM pcpicker_cpucooler WHERE noise_level < 30;

    Q: Which monitor has the highest refresh_rate?  
    A:
    SELECT name, refresh_rate FROM pcpicker_monitor ORDER BY refresh_rate DESC LIMIT 1;

    Q: List all motherboards that support the AM4 socket  
    A:
    SELECT name FROM pcpicker_motherboard WHERE socket_cpu = 'AM4';

    ---

    Now, based on the schema and rules above, generate the SQL query for the user’s question below.

    Question:
    {query}

    ---

    Only return the SQL query. Do not add any explanation or comments.

    """

    try:
        
        response = ollama.chat(model="qwen2.5:1.5b-instruct-fp16", messages=[{"role": "user", "content": sql_prompt}])
        output= response['message']['content'].strip()
        clean_sql = output.replace("```sql", "").replace("```", "").strip()
        print(clean_sql)
        return clean_sql
    except Exception as e:
        return f"Error during chat: {str(e)}"
    
def query_answer(sql_query):
    try:
        conn= sqlite3.connect(r"C:\Users\pavit\programing\pcpickertool\db.sqlite3")
        print("SQL query is:", sql_query)
        print("Type of sql_query:", type(sql_query))
        df= pd.read_sql_query(sql_query,conn)
        print("df  :  ",df)
        conn.close()
        if df.empty:
            return "no data found"
        markdown_table = df.to_markdown(index=False)
        print(markdown_table)
        return markdown_table
    except Exception as e:
        return f"❌ Error running SQL: {str(e)}"

def get_ollama_answer(query: str) -> str:
    
    context,type=hybrid_method(query)
    print(context)

    if type=="webiste":
        final_prompt = f"""
                You are a helpful and intelligent chatbot assistant built for a PC Picker Tool website.

                ### Your Role:
                You assist users in understanding and navigating the **website's features and functionalities**. Users may ask you:
                - What the website does
                - How to use certain features (e.g., saving a build, changing components, viewing summaries)
                - Clarifications or help on how to interact with the tool
                - Steps for using the platform (e.g., "How do I start building?", "Can I change my GPU later?")
                - Issues they face (e.g., "I can't see my saved build", "How do I reset all components?")

                You will always be given:
                - A **user query**
                - A **retrieved paragraph (context)** from the website’s help system or documentation

                ### Your Job:
                - Read and understand the paragraph provided
                - Use it to answer the user’s question clearly and helpfully
                - Do NOT invent features or provide guesses — stick only to what's in the context

                ---

                User Query:
                "{query}"

                Context:
                {context}

                ---

                Respond to the user using ONLY the context above.
                If the context doesn't provide the answer, politely state that it's not available.
                """
        try:
            response = ollama.chat(
                model="qwen:1.8b-chat",
                messages=[{"role": "user", "content": final_prompt}],
                
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Error during chat: {str(e)}"
   

    elif type=="SQL":
        final_prompt = f"""
                You are a technical assistant chatbot for the PC Picker Tool.

                ### Your Role:
                You help users with **PC component-related technical queries** using real structured data from the database. The user may ask:
                - Which CPU or GPU has the best performance
                - What components meet specific requirements (e.g., low TDP, high cores, specific sockets)
                - Comparisons, filtering, or sorting of parts based on specs

                You will always be given:
                - A **user query**
                - A **markdown table** which contains filtered data from the database based on their question

                ### Your Job:
                - Read the markdown table carefully like a data analyst
                - Use ONLY this table to generate a **clear, accurate response**
                - You can explain or summarize the result, but must **not use any external knowledge**
                - If the answer is evident from the table, state it. If not found, say no matching result.

                Important:
                - You are NOT supposed to generate new SQL queries now.
                - You are only answering based on already executed SQL results passed in table format.

                ---

                User Query:
                "{query}"

                Markdown Table:
                {context}

                ---

                Answer based ONLY on this table.
                Do not assume anything not shown here.
                """
        try:
            response = ollama.chat(
                model="qwen:1.8b-chat",
                messages=[{"role": "user", "content": final_prompt}],
                
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Error during chat: {str(e)}"
                
