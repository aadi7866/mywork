import transformers
import streamlit as st
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="osei1819/phishing_detection_fine_tuned_bert",truncation=True, max_length=256)
st.title("Phishing Detection")

input=st.text_area("write the testing text")
if st.button("check") and input!="":
 result=pipe(input)
 st.subheader("Lable")
 st.write(result[0]["lable"])
 st.subheader("Modle Confidance")
 st.write(result[0]["score"])
