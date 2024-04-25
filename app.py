import streamlit as st
from openai import OpenAI

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
#local_css("style.css")


f = open("key.txt")
OPENAI_API_KEY = f.read()

st.title("GENAI Code Reviewer")
st.subheader("Welcome to GENAI Code reviewer")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_area("Enter your Code")
height=400

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code with comments.You can also provide alternative better code"},
        {"role": "user", "content": prompt}
      ]
    )

    st.write(response.choices[0].message.content)