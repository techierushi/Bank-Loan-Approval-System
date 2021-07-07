import streamlit as st

html_temp = """
<div style ="background-color:#acf07f;padding:13px">
<h1 style ="color:black;text-align:center;font-family: Garamond, serif;font-size:43px;"> Bank Personal Loan <br> Recommender System </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

st.markdown("""
<h3><center> Check whether a potential customer (Depositor) <br> will buy the personal loan or not </center></h3>
"""
,unsafe_allow_html = True)
