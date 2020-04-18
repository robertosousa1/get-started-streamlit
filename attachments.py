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
    st.text('1. Attaching an image')
    st.image('https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e18182db827fa0659541754_RGB_Logo_Vertical_Color_Light_Bg-p-1600.png', width=100)
    st.text('2. Attaching an audio')
    st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg')
    st.text('3. Attaching a video')
    st.video('https://www.youtube.com/watch?v=_lOT2p_FCvA')

if __name__ == '__main__':
    main()