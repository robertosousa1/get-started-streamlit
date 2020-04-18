import streamlit as st
import pandas as pd

def main():
    st.title('Hello, Streamlit!')
    st.header('A simple repository containing some steps to get started with the Stream library.')
    st.text('\n')
    st.subheader('For more details see the documentation:')
    st.subheader('https://docs.streamlit.io/api.html')
    st.text('\n\n')
    st.subheader('Examples:')
    st.text('\n')
    st.markdown('1. Display a dataframe:')
    file = st.file_uploader('Choose your file', type='csv')
    if file is not None:
        slider = st.slider('Values', 1, 100)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.text('\n')
        st.table(df.head(slider))
        st.text('\n')
        st.write(df.columns)
        st.table(df.groupby('species')['petal_width'].mean())


if __name__ == '__main__':
	main()