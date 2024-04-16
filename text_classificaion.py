import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

# Load the tokenizer and model once
tokenizer = AutoTokenizer.from_pretrained("vishnun0027/Text_classification_model_10042024")
model = AutoModelForSequenceClassification.from_pretrained("vishnun0027/Text_classification_model_10042024")

def classify_text(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")
    
    # Perform the classification
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Get the predicted class ID
    predicted_class_id = logits.argmax().item()
    
    # Convert the class ID to a label
    predicted_class_label = model.config.id2label[predicted_class_id]
    
    return predicted_class_label