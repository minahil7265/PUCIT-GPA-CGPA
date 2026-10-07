import streamlit as st
from langchain.messages import HumanMessage

from agent import ask

st.set_page_config(page_title="PUCIT GPA/CGPA Advisor", page_icon="🎓")
st.title("PUCIT GPA/CGPA Advisor")
st.caption(
    "Ask about a semester GPA, a projected CGPA, or what you need to hit a "
    "target CGPA. The agent will show you the calculations and reasoning behind its answers."
)

if "history" not in st.session_state:
    st.session_state.history = []  # full LangChain message history
if "display" not in st.session_state:
    st.session_state.display = []  # (role, text) pairs for rendering

for role, text in st.session_state.display:
    with st.chat_message(role):
        st.markdown(text)

user_input = st.chat_input("Type your question...")

if user_input:
    st.session_state.display.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.history = st.session_state.history + [HumanMessage(user_input)]

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply_text, st.session_state.history = ask(st.session_state.history)
        st.markdown(reply_text)

    st.session_state.display.append(("assistant", reply_text))

with st.sidebar:
    st.subheader("About")
    st.write(
        "This agent calculates GPA, CGPA "
        "and the required GPA to hit a target CGPA. "
    )
    if st.button("Reset conversation"):
        st.session_state.history = []
        st.session_state.display = []
        st.rerun()
