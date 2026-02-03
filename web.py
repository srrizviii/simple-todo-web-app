import streamlit as st
import todo_functions as tf

todos = tf.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    tf.write_todos(todos)

st.title("My To-Do App")
st.write("A simply way to track what you need to get done.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: 
        todos.pop(index)
        tf.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")