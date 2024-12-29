import openai

openai.api_key = 'your_openai_api_key'

def paraphrase_text(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Paraphrase the following text:\n\n{text}",
        max_tokens=1000
    )
    return response.choices[0].text.strip()
