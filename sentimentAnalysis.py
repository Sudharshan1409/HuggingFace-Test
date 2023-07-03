from transformers import pipeline

generator = pipeline("sentiment-analysis")
sentences = [
    "I'm happy to learn how to build apps with HuggingFace",
    "HuggingFace is based in New York City",
    "HuggingFace is not bad",
    "HuggingFace is shit",
    "I'm going to sleep",
    "I woke up just now"
]
outputs = generator(sentences)

for i, output in enumerate(outputs):
    print(sentences[i], output)