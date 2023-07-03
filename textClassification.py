from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

res = classifier(
    input("Enter the sentence: "),
    candidate_labels = list(input("Enter the Categories: ").split())
)

for i, label in enumerate(res['labels']):
    print(label, res['scores'][i])