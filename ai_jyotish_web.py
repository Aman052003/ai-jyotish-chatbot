import streamlit as st

st.set_page_config(page_title="AI Jyotish Chatbot", page_icon="🔮", layout="centered")

st.title("🔮 AI Jyotish Chatbot")
st.markdown("Namaste! Main ek AI-based Jyotish chatbot hoon. Apna prashn poochhiye:")

user_input = st.text_input("🗣️ Aapka prashn yahan likhiye:")

if user_input:
    # Dummy future prediction logic
    st.markdown(f"🧘‍♂️ Aapka bhavishya kehata hai: **'{user_input}'** ka uttar safalta se milega, lekin dhairya rakhna hoga. 🌟")
