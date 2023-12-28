from transformers import pipeline
import gradio as gr

#reference appropriate Hugging Face model
model_name = 'koakande/bert-finetuned-ner'

# Load token classification pipeline modelfrom Hugging Face
model = pipeline("token-classification", model=model_name, aggregation_strategy="simple")

# write a prediction method for the model
def predict_entities(text):
    # Use the loaded model to identify entities in the text
    entities = model(text)
    # Highlight identified entities in the input text
    highlighted_text = text
    for entity in entities:
        entity_text = text[entity['start']:entity['end']]
        replacement = f"<span style='border: 2px solid green;'>{entity_text}</span>"
        highlighted_text = highlighted_text.replace(entity_text, replacement)
    return highlighted_text

# gradio interface
title = "Named Entity Recognizer"

description = """
This model has been trained to identify entities in a given text. It returns the input text with the entities highlighted in green. Give it a try!
"""

article = "The model is trained using bert-finetuned-ner."

iface  = gr.Interface(
    fn=predict_entities,
    inputs=gr.Textbox(lines=5, placeholder="Enter text..."),
    outputs=gr.HTML(),
    title=title,
    description=description,
    article=article,
    examples=[["Hello, I am Kabeer. I work as a machine learning engineer at OVO in the UK"], ["This is Maryam who is a Leicester based NHS Doctor"]],
)

iface.launch()