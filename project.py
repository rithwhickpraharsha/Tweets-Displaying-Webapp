import streamlit as st
import streamlit.components.v1 as components
import requests
st.set_page_config(page_title="embedder", page_icon=":baby_chick:", layout="wide")


st.subheader("Embending tweets : ")
st.write("python based streamlit app")

components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="153967/"></script> <!-- end feedwind code -->',height=700)

st.write("Child abuse")
components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="153967/"></script> <!-- end feedwind code -->',height=700)
st.write("CID")
components.html('<!-- start feedwind code --> <script type="text/javascript" src="https://feed.mikle.com/js/fw-loader.js" preloader-text="Loading" data-fw-param="153967/"></script> <!-- end feedwind code -->',height=700)
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
