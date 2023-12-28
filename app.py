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
iface = gr.Interface(
    fn=predict_entities,
    inputs=gr.Textbox(lines=5, placeholder="Enter text..."),
    outputs=gr.HTML(),
    title="Named Entity Identification",
    description="Enter text to identify entities using the model.",
)

iface.launch()