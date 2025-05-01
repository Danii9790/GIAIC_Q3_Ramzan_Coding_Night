import os
import chainlit as cl
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional,Dict
load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model=genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.oauth_callback
def aauth_callback(
    provider_id:str,
    token:str,
    raw_user_data: Dict[str,str],
    default_user : cl.User,
) -> Optional[cl.User]:
    """ 
    Handle the OAuth callback from Github
    Return the user object if authentication is sucessfull , Otherwise None
    """
    print(f"Provider Id : {provider_id}")
    print(f"User data : {raw_user_data}")
    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("histroy",[])

    await cl.Message(content="Hello! How can i help you today?").send()

@cl.on_message
async def handle_message(message : cl.Message):
    histroy= cl.user_session.get("histroy")
    histroy.append({"role":"user","content":message.content})

    formatted_histroy=[]
    for msg in histroy:
        role= "user"  if msg["role"]=="user" else "model"
        formatted_histroy.append({"role":role,"parts":[{"text":msg["content"]}]})
    
    response= model.generate_content(formatted_histroy)

    response_text=response.text if hasattr(response,"text") else ""
    
    histroy.append({"role":"assistant", "content":response_text})

    cl.user_session.set("histroy",histroy)

    await cl.Message(content=response_text).send()
