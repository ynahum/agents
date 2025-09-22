import os
from typing import Dict

import resend
from agents import Agent, function_tool

@function_tool
def send_email(subject:str, body: str):
    """ Send out an email with the given body to all sales prospects """
    resend.api_key = os.environ.get('RESEND_API_KEY')
    
    params = {
        "from": "onboarding@resend.dev",  # Change to your verified sender domain
        "to": "ynahum@gmail.com",  # Change to your recipient
        "subject": subject,
        "html": body
    }
    
    response = resend.Emails.send(params)
    return {"status": "success"}

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)
