import os
from dotenv import load_dotenv
import gradio as gr


load_dotenv()


API_KEY = os.getenv('API_KEY')


class SimpleConversationAgent:
    def __init__(self, model_name):
        self.model_name = model_name
        self.context = ""

    def respond(self, user_input):
       
        if "funny" in self.model_name:
            return f"Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!"
        elif "medical" in self.model_name:
            return f"Medical Report: Patient shows signs of improvement."
        else:
            return f"Response from model {self.model_name}: You asked about '{user_input}'"


def select_model(model_name):
    agent = SimpleConversationAgent(model_name)
    return agent


def chat(model_name, user_input):
    agent = select_model(model_name)
    response = agent.respond(user_input)
    return response


with gr.Blocks() as interface:
    gr.Markdown("# AI Chatbot")
    model_name = gr.Dropdown(choices=["funny-bot", "medical-bot", "default-bot"], label="Select Model")
    user_input = gr.Textbox(label="Your message")
    

    chatbot_output = gr.Textbox(label="Chatbot Response")
    submit_btn = gr.Button("Submit")
    submit_btn.click(fn=chat, inputs=[model_name, user_input], outputs=chatbot_output)


interface.launch()
