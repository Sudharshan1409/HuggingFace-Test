from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
import sys

line = "What is the capital of France?"
model_name = 'google/flan-t5-base'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = GenerationConfig(max_new_tokens=200)
tokenizer = AutoTokenizer.from_pretrained(model_name)

while True:
    line = input("You: ")
    tokens = tokenizer(line, return_tensors='pt')
    print('tokens', tokens)
    outputs = model.generate(**tokens, generation_config=config)
    print(tokenizer.batch_decode(outputs, skip_special_tokens=True))