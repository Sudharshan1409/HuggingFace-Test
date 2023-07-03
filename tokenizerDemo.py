from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
import sys

line = "Which is the country where people are very unhappy?"
model_name = 'google/flan-t5-base'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = GenerationConfig(max_new_tokens=200)
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokens = tokenizer.tokenize(line)
ids = tokenizer.convert_tokens_to_ids(tokens)
print('tokens', tokens)
print('ids', ids)
tokens = tokenizer(line, return_tensors='pt')
input_embeddings = model.get_input_embeddings()
token_ids = tokens['input_ids'][0]
embeddings = input_embeddings(token_ids)
print('embeddings', embeddings)
print('embeddings.shape', embeddings.shape)