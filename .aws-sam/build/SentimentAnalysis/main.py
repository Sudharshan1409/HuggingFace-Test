from transformers import pipeline
import os
import json
def lambda_handler(event, context):
    # TODO implement
    print("Hello World")
    print(os.listdir("/mnt/efs"))
    # check if the directory exists
    if not os.path.exists("/mnt/efs/sentimentAnalysis/models"):
        os.makedirs("/mnt/efs/sentimentAnalysis/models")
    generator = pipeline("sentiment-analysis", model="/mnt/efs/sentimentAnalysis/models")
    sentences = [
        "I'm happy to learn how to build apps with HuggingFace",
        "HuggingFace is based in New York City",
        "HuggingFace is not bad",
        "HuggingFace is shit",
        "I'm going to sleep",
        "I woke up just now"
    ]
    outputs = generator(sentences)
    formatted_output = {}
    for i, output in enumerate(outputs):
        print(sentences[i], output)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
