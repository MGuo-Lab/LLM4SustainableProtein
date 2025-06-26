from openai import OpenAI
import pandas as pd
import json
from tqdm import tqdm

# Configure key variables
API_KEY = 'YOUR-API-KEY'  # Change to your own OpenAI API key
TSV_FILE = 'final_prompts_assigned.tsv'
TRAIN_JSONL = 'train.jsonl'
VAL_JSONL = 'val.jsonl'
TEST_JSONL = 'test.jsonl'
TEST_TSV = 'prompts_table.tsv'
MODEL = 'gpt-4.1-2025-04-14'

# Initiate OpenAI API with key
client = OpenAI(api_key=API_KEY)

# Load data into dataframe
df = pd.read_csv(TSV_FILE, sep='\t')

# Split into training, validation and testing dataframes
train_df = df[df['assignment'] == 'train']
val_df = df[df['assignment'] == 'val']
test_df = df[df['assignment'] == 'test']

# Function for formatting data into format for OpenAI API
def to_chat_format(prompt, response):
    return {
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt},
            {'role': 'assistant', 'content': response}
        ]
    }

# Function for saving json files
def save_jsonl(df, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        for _, row in tqdm(df.iterrows(), total=len(df)):
            f.write(json.dumps(to_chat_format(row['prompt'], row['ideal_response'])) + '\n')

# Save json files, for use with OpenAI API
save_jsonl(train_df, TRAIN_JSONL)
save_jsonl(val_df, VAL_JSONL)
test_df.to_csv(TEST_TSV, sep='\t', index=False)

# Configure json files via OpenAI API
train_file = client.files.create(file=open(TRAIN_JSONL, 'rb'), purpose='fine-tune')
val_file = client.files.create(file=open(VAL_JSONL, 'rb'), purpose='fine-tune')

# Print training and validation json file IDs
print('Training file ID:', train_file.id)
print('Validation file ID:', val_file.id)

# Start fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=train_file.id,
    validation_file=val_file.id,
    model=MODEL,
    hyperparameters={
        'n_epochs': 10  # Set desired number of epochs
    }
)

# Print job ID to console
print('Fine-tuning job started. Job ID:', job.id)

