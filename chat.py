from transformers import AutoTokenizer, BlenderbotForConditionalGeneration, GenerationConfig

mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)

config = GenerationConfig(max_new_tokens=200)
sentences = []
while True:
    user_input = input("You: ")
    sentences.append(user_input)
    inputs = tokenizer(user_input, return_tensors="pt")
    reply_ids = model.generate(**inputs,  generation_config=config)
    response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    print("Bot:", response)
    sentences.append(response)