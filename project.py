import streamlit as st
import streamlit.components.v1 as components
import requests
import time
import webbrowser
from io import StringIO
import pandas as pd

from PIL import Image
st.set_page_config(page_title="embedder", page_icon=":baby_chick:", layout="wide")

st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">{"WOMEN HARSAMENT ”"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#FF0000;font-size:36px;">{"AND "}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">{"CYBER CRIME”"}</h1>', unsafe_allow_html=True)

st.write("python based streamlit app")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
    
)

# Using "with" notation
with st.sidebar:
   
    add_radio = st.selectbox(
        "contact details: ",
        ("prateek rajesh", "rithwhick")
    )
    st.markdown(f'<h1 style="color:#FF0000;font-size:px;">{"WOMEN HARSAMENT ”"}</h1>', unsafe_allow_html=True)


img = Image.open("woman.jpg")

st.image(img,width=1025)
st.subheader("Women harrasment")

components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154406/"></script> <!-- end feedwind code -->',height=450)
st.subheader("Child abuse")
img = Image.open("cabuse.jpg")

st.image(img,width=1025)

components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154407/"></script> <!-- end feedwind code -->',height=450)
st.subheader("Cyber Bully")
img = Image.open("Cyberbullying.png")

st.image(img,width=1025)
components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154406/"></script> <!-- end feedwind code -->',height=450)
st.subheader("CyberCrime")
img = Image.open("cyber.jpg")

st.image(img,width=1025)
components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="154406/"></script> <!-- end feedwind code -->',height=450)

uploaded_file = st.file_uploader("share your experiences in .txt formate ")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-16"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     #st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)


# def theTweet(tweet_url):
#     api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
#     response = requests.get(api)
#     res = response.json()["html"]
#     print(res)
#     return f'<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="153967/"></script> <!-- end feedwind code -->'

# input = st.text_input("Enter your tweet url")
# if input:
#     res = theTweet(input)
 
#     components.html(res,height= 700)
