import streamlit as st

import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"]=""

st.title("My To-Do app")
st.subheader("This is my todo app")
st.write("This app will improve your <b>productivity</b>",unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo",key="new_todo", on_change=add_todo )



