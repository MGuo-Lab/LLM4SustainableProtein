from sentence_transformers import SentenceTransformer, util


# List of SBERT models
# (Note that sentence-t5-base is technically not an SBERT model)
sbert_models = ['all-mpnet-base-v2', 'all-MiniLM-L6-v2', 'sentence-t5-base']

# Two sentences, with similar meaning but different wording.
sentence1 = 'Yesterday, the cat climbed up a tree.'
sentence2 = 'A tree was climbed by the domestic feline, the day before today.'


# Iterate through SBERT models.
for sbert_model in sbert_models:
    
    print(sbert_model)
    
    # Define model.
    model = SentenceTransformer(sbert_model)
    
    # Compute embeddings.
    embeddings = model.encode([sentence1, sentence2], convert_to_tensor=True)
    # Compute cosine similarity between embeddings.
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
        
    print(f'Simlarity score: {similarity}')
