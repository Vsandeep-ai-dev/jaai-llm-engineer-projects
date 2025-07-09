import openai
import os

def get_gpt_feedback(parsed_data):
    prompt = f"""You are a career coach. Review this resume data and give 3 strengths, 3 weaknesses, and suggestions to improve it for job applications:
    
{parsed_data}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message["content"]
