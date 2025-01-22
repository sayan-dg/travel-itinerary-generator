from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import ast


groq_api_key = "your-groq-api-key"

llm = ChatGroq(groq_api_key=groq_api_key, model='llama3-70b-8192')

def llm_response(city, days):
    template = """
    You are a travel itinerary generator. Generate a list of places to visit
    in {city} in {days} days. Give output as a python list. Each item of the
    list should be places to visit on each day. Just provide the names of the
    places to visit each day separated by comma. Provide only the list as output
    no extra text. A sample output is for 5 places to visit in 2 days as follows:
    "['Place 1, Place 2', 'Place 3, Place 4, Place 5']"
    """
    prompt_template = PromptTemplate(input_variables = ['city', 'days'],
                                     template = template)
    
    chain = prompt_template | llm
    
    inputs = {'city':city, 'days':days}
    
    response = chain.invoke(inputs)
    
    response_list = ast.literal_eval(response.content)
    
    return response_list