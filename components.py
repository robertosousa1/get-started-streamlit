import streamlit as st

def main():
    st.title('Hello, Streamlit!')
    st.header('A simple repository containing some steps to get started with the Stream library.')
    st.text('\n')
    st.subheader('For more details see the documentation:')
    st.subheader('https://docs.streamlit.io/api.html')
    st.text('\n\n')
    st.subheader('Examples:')
    st.text('\n')
    st.markdown('1. Button')
    button = st.button('Button')
    if button:
        st.markdown('Button clicked!')
    st.text('\n')
    check = st.checkbox('2. Checkbox')
    if check:
        st.markdown('Checkbox clicked!')
    st.text('\n')
    st.markdown('3. Radio')
    radio = st.radio('Choose options:', ('Option 1', 'Option 2', 'Option 3'))
    if radio == 'Option 1':
        st.markdown('Option 1, chosen!')
    if radio == 'Option 2':
        st.markdown('Option 2, chosen!')
    if radio == 'Option 3':
        st.markdown('Option 3, chosen!')
    st.text('\n')
    st.markdown('4. Selectbox')
    select = st.selectbox('Choose option:', ('Option 1', 'Option 2', 'Option 3'))
    if select == 'Option 1':
        st.markdown('Option 1, chosen!')
    if select == 'Option 2':
        st.markdown('Option 2, chosen!')
    if select == 'Option 3':
        st.markdown('Option 3, chosen!')
    st.text('\n')
    st.markdown('5. Multiselect')
    multi = st.multiselect('Choose options:', ('Option 1', 'Option 2', 'Option 3'))
    if multi == 'Option 1':
        st.markdown('Option 1, chosen!')
    if multi == 'Option 2':
        st.markdown('Option 2, chosen!')
    if multi == 'Option 3':
        st.markdown('Option 3, chosen!')
    st.text('\n')
    st.markdown('6. File Uploader')
    file = st.file_uploader('Choose your file', type='csv')
    if file is not None:
        st.markdown('It is not empty!')
    st.text('\n')

if __name__ == '__main__':
    main()