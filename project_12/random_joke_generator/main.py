import streamlit as st 
import requests

def random_joke():
    """ Fetch a random joke from the Api """
    try:
        response=requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data=response.json()
            return f"{joke_data ['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke.Please try again Later."
    except Exception as e:
        return f"An error occured {e}"
    
def main():
    st.set_page_config(page_title="Random_Joke")
    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random Joke.")
    if st.button("Generate Joke"):
        joke =random_joke()
        st.success(joke)
    
    st.divider()
    st.markdown(
        """
    <div style='text-align:center'>
    <p style='text-bold'>Joke from Official joke Api </p>
    <p>Bulid with ❤ by <a href='https://github.com/Danii9790'>Muhammad Daniyal </a> Using Streamlit</p>
    </div>
""",
        unsafe_allow_html=True
    )

if __name__=='__main__':
    main()

