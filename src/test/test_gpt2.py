import os, sys
sys.path.append(os.getcwd())

from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import pipeline

model_path = "/Users/diniu/Documents/models/gpt2"

# tokenizer = GPT2Tokenizer.from_pretrained(model_path)
# model = GPT2LMHeadModel.from_pretrained(model_path)

generator = pipeline('text-generation', model=model_path)
# out = generator("I can't believe you did such a ", max_length=100, num_return_sequences=1)
query = "I can't believe you did such a "

query = "System: Let's first understand the problem and devise a plan to solve the problem. Please output the plan starting with the header 'Plan:'  and then followed by a numbered list of steps. Please make the plan the minimum number of steps required to accurately complete the task. If the task is a question, the final step should almost always be 'Given the above steps taken, please respond to the users original question'. At the end of your plan, say '<END_OF_PLAN>\n\n User: Who is Leo DiCaprio's girlfriend?\n\nAssistant:"

out = generator(
    query,
	max_new_tokens=50,
    # num_beams=5,
    # do_sample=True,
	num_return_sequences=1,
    penalty_alpha=0.6, top_k=4,
)
print(out)
