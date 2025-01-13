import transformers
import streamlit as st
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="osei1819/phishing_detection_fine_tuned_bert",truncation=True, max_length=256)


input=st.text_area("write the testing text")

result=pipe(input)
st.write(result)
