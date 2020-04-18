import streamlit as st
import pandas as pd
import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Click here</a>'
    return href

def main():
    st.title('Hello, Streamlit!')
    st.header('A simple repository that contains the steps of pre-processing data with Python using Streamlit and '
              'Pandas.')
    st.text('\n\n')
    file = st.file_uploader('Choose your file', type='csv')
    if file is not None:
        st.subheader('Analyze the data')
        df = pd.read_csv(file)
        st.markdown('**Number of lines:**')
        st.markdown(df.shape[0])
        st.markdown('**Number of columns:**')
        st.markdown(df.shape[1])
        st.text('\n\n')
        st.markdown('**View the dataframe:**')
        number = st.slider('Choose the number of columns:', min_value=1, max_value=20)
        st.dataframe(df.head(number))
        st.markdown('**Name of columns:**')
        st.markdown(list(df.columns))
        st.text('\n\n')
        exploration = pd.DataFrame({
            'names': df.columns,
            'types': df.dtypes,
            'NA #': df.isna().sum(),
            'NA %': (df.isna().sum() / df.shape[0]) * 100
        })
        st.markdown('**Count of data types:**')
        st.write(exploration.types.value_counts())
        st.markdown('**Column names of type int64:**')
        st.markdown(list(exploration[exploration['types'] == 'int64']['names']))
        st.markdown('**Column names of type float64:**')
        st.markdown(list(exploration[exploration['types'] == 'float64']['names']))
        st.markdown('**Column names of type object:**')
        st.markdown(list(exploration[exploration['types'] == 'object']['names']))
        st.markdown('**Table with column and percentage of missing data:**')
        st.table(exploration[exploration['NA #'] != 0][['types', 'NA %']])
        st.text('\n')
        st.subheader('Numeric data entry:')
        percentage = st.slider(
            'Choose the missing percentage limit for the columns you want to input data', min_value=0, max_value=100
        )
        list_columns = list(exploration[exploration['NA %'] < percentage]['names'])
        select_method = st.radio('Choose a method below:', ('Mean', 'Median'))
        st.markdown('You have selected: ' + str(select_method))
        if select_method == 'Mean':
            df_input = df[list_columns].fillna(df[list_columns].mean())
            exploration_input = pd.DataFrame({
                'names': df_input.columns,
                'types': df_input.dtypes,
                'NA #': df_input.isna().sum(),
                'NA %': (df_input.isna().sum() / df_input.shape[0]) * 100
            })
            st.table(exploration_input[exploration_input['types'] != 'object']['NA %'])
            st.subheader('Download: ')
            st.markdown(get_table_download_link(df_input), unsafe_allow_html=True)
        if select_method == 'Median':
            df_input = df[list_columns].fillna(df[list_columns].mean())
            exploration_input = pd.DataFrame({
                'names': df_input.columns,
                'types': df.dtypes,
                'NA #': df_input.isna().sum(),
                'NA %': (df_input.isna().sum() / df_input.shape[0]) * 100
            })
            st.table(exploration_input[exploration_input['types'] != 'object']['NA %'])
            st.subheader('Download: ')
            st.markdown(get_table_download_link(df_input), unsafe_allow_html=True)

if __name__ == '__main__':
	main()