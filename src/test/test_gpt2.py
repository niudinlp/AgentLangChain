import os, sys
sys.path.append(os.getcwd())

from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import pipeline, set_seed

model_path = "/Users/diniu/Documents/models/gpt2"

# tokenizer = GPT2Tokenizer.from_pretrained(model_path)
# model = GPT2LMHeadModel.from_pretrained(model_path)

generator = pipeline('text-generation', model=model_path)
out = generator("I can't believe you did such a ", max_length=100, num_return_sequences=1)
print(out)
