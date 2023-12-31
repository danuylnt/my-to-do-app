import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title('My to do app')
st.subheader('Hello')
st.write('To increase prod')

for index, todo in enumerate(todos):
    checkbox_key = f"{todo}_{index}"
    checkbox = st.checkbox(todo, key=checkbox_key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[checkbox_key]
        st.experimental_rerun()

st.text_input(label='',placeholder = 'Add a new todo...',
              on_change=add_todo, key='new_todo')

