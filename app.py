import streamlit as st
from llm_response import llm_response

st.header("Tour Itinerary Generator")

city = st.text_input("Enter the name of the city you wish to travel")

days = st.selectbox("For how many days do you want to travel?",
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

generate = st.button("Generate")

if generate:
    
    if city and days:
        
        itinerary_list = llm_response(city, days)
        
        for day_number in range(len(itinerary_list)):
            
            st.write("Day ",str(day_number+1),": ", itinerary_list[day_number])
            
    else:
        
        st.write("Enter city and number of travel days")
        
    
    