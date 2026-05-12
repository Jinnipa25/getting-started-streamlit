import streamlit as st
import pandas as pd

with st.echo():
    st.title("Getting Started Streamlit")
    st.write("This is intoduction to streamlit")

    st.markdown("## Code")
    code = '''
    def hello(): 
        print("Hello, Streamlit!)
    '''

    show_btn = st.button("Showcode!")
    if show_btn:
        st.code(code, language='python')


    cols = st.columns(2)
    with cols[0]:
        age_input = st.number_input("Input your age")
        st.markdown(f"Your age is {age_input}")

    #st.markdow("# NLP Task")
    with cols[1]:
        text_inp = st.text_input("Input your text",)
        word_tokenize = "|".join(text_inp.split())
        st.markdown(f"{word_tokenize}")


    df = pd.DataFrame({
        'first column':[1,2,3,4],
        'second column': [10,20,60,99]
    })
    st.dataframe(df)


    line_chart_btn = st.button("Show Line chart!")
    if line_chart_btn:
        st.line_chart(df, x='first column', y ='second column')