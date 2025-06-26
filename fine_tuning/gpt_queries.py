from openai import OpenAI

# Specify model name
model_name = 'gpt-4.1-2025-04-14'

# Specify temperature
temp = 0.0

# Load your API key securely
client = OpenAI(api_key='YOUR-API-KEY')  # Change to your own OpenAI API key

# Specify microbial strain
microbe_strain = 'Thermomonospora fusca'

# Specify pdf text for study (shallow example provided)
pdf_text = '''The study found that Thermomonospora fusca yields 80% protein (dry mass).
The study also reports a hetero trophic mechanism.
The following substrates are reported: cellulose and hemicellulose.
These are of a lignocellulosic resource substrate class.
'''

# Define prompt
prompt = f'''For the genus species {microbe_strain}, please find the reported protein % dry mass, trophic mechanism, reported substrate and substrate class, from the following paper(s).

Please give your answer in a concise "reported protein % dry mass: [answer], trophic mechanism: [answer], reported substrate: [answer], substrate class: [answer]" format.

If the information cannot be found, then please respond with: "The literature provided does not contain the requested information, for the microbial species specified."

Find the information from the PDF text of the following paper(s):

{pdf_text}
'''
    
# Safe try-loop
try:
    # Send API query to the GPT model
    response = client.chat.completions.create(
        model=model_name,
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': prompt}],
        temperature=temp,
        max_tokens=500
    )
    # Obtain response
    result = response.choices[0].message.content
# Obtain error message, if error occurs
except Exception as e:
    result = f'Error: {e}'

# Print response and handle it as appropriate.
print(result)
