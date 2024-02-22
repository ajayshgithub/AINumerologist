from dotenv import load_dotenv
load_dotenv()    ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Initializing our Gemini Pro mOdel and get responses

model = genai.GenerativeModel('gemini-pro')
def get_gemini_responses(question):
    response=model.generate_content(question)
    return response.text

## Initialize our streamlit app

st.set_page_config(page_title="AiNumerologist")

st.header("Gemini Astrotalk")

input=st.text_input("Enter DOB: ",key="input")   ##text box

submit=st.button("Ask About Yourself")

input_prompt="""
You are an expert numerologist and have a deep knowledge of numerology and astrology .
Based on your deep understanding in numerology you can tell about a person by just his date of birth. 
Given a user's date of birth(format = date-month-year) input,
implement functionality and all your numerological and astrological to calculate and display the following in the format:

1. Driver Number: Your birth date(usually between 0-9, if date is 11 then It will be counted as 1+1=2) 
2. Destiny Number: Destiny number using the provided date(sum of whole dob and a single digit as driver number).
3. Positive Traits: Identify and list positive personality traits associated with the user's numerological profile.
4. Negative Traits: Identify and list negative personality traits associated with the user's numerological profile.
5. Future Career Options: Provide insights into potential future career paths based on the user's numerological profile.

Ensure that the output is clear, very detailed and presented in an easily understandable format within the existing app interface.
Also remember that all the point mentioned above should be covered.
"""

if submit:
    response=get_gemini_responses(input)
    st.subheader("The Response is")
    st.write(response)