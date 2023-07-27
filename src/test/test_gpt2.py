import os, sys
sys.path.append(os.getcwd())

from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import pipeline, set_seed

model_path = "/Users/diniu/Documents/models/gpt2"

# tokenizer = GPT2Tokenizer.from_pretrained(model_path)
# model = GPT2LMHeadModel.from_pretrained(model_path)

generator = pipeline('text-generation', model=model_path)
# out = generator("I can't believe you did such a ", max_length=100, num_return_sequences=1)
out = generator(
    "I can't believe you did such a ",
	max_new_tokens=50,
    # num_beams=5,
    # do_sample=True,
	num_return_sequences=1,
    penalty_alpha=0.6, top_k=4,
)
print(out)
