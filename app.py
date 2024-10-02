import json 
import streamlit as st
import requests   
import json
import boto3 
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from dotenv import load_dotenv
import os
from pprint import pprint
from io import StringIO

load_dotenv()
session = boto3.Session(
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name = os.environ.get('AWS_DEFAULT_REGION')
)
credentials = session.get_credentials()

# Streamlit app code
page_title = "GENAI Innovators Canada"
page_icon = "⚡"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# --- HIDE STREAMLIT STYLE ---
streamlit_style = """
    <style>
    footer {visibility: hidden;}
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
    html, body, [class*="css"]  {
    font-family: 'Roboto', sans-serif;
    }
    </style>
"""
st.markdown(streamlit_style, unsafe_allow_html=True)

def query_api(user_input):
    url = "https://pyvlvu7m39.execute-api.us-east-1.amazonaws.com/staging/"
    payload = {"query": user_input}
    api_headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=api_headers) 
        request = AWSRequest(method='POST', url=url, data=json.dumps(payload))
        SigV4Auth(credentials, 'execute-api', 'us-east-1').add_auth(request)

        headers = dict(request.headers.items())
        response = requests.post(url, json=payload, headers=headers)
        json_string = response.json()

        return json_string
    
    except requests.RequestException as e:
        st.error(f"An error occurred: {str(e)}")
        return None

if __name__ == '__main__':
    st.title('Transformer health :blue[knowledge base, and search]')
    description = """A cutting-edge solution designed to deliver insights into transformer performance while also alerting users when health statistics exceed industry specified standards.  """
    st.write(description)
    st.sidebar.markdown("""⚡[GENAI Innovators Canada](https://capgemini.awshackathon.onova.io/live/submission)
                        A group of curious individuals exploring the power of generative AI to create exciting new solutions.
                        """, unsafe_allow_html=True) 

    # Streamlit UI
    st.subheader("Transformer Query")
    user_input = st.text_input("Enter your query:")

    if st.button("Submit"):
        if user_input:
            with st.spinner("Searching..."):
                json_string = query_api(user_input) 
            
            st.write("Response:") 
            
            # Pretty print the JSON 
            print(json_string)
            if 'body' in json_string:
                body_content = json_string['body']
                inner_json = json.loads(body_content)
                response = inner_json['response']
                st.write(response)

        else:
            st.warning("Please enter a query.")