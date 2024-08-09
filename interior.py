import streamlit as st
import torch
import numpy as np
from scipy.special import softmax
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSequenceClassification
from PIL import Image


def feature_extraction(text):
    model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    #     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = AutoModelForSequenceClassification.from_pretrained(model_id)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    return output


def get_output_scores(text):
    with torch.no_grad():
        output = feature_extraction(text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        return scores


def get_rating(description):
    output_array = get_output_scores(description)
    max_score = max(output_array)
    max_index = output_array.argmax()
    if max_index == 0:
        return round((1 - max_score) * 10, 1)
    else:
        return round(max_score * 10, 1)


def model_init():
    model_id = "vikhyatk/moondream2"
    revision = "2024-04-02"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision
    ).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    return model, tokenizer


def main():
    model, tokenizer = model_init()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    #     prompt = """As an interior quality assessor, your task is to analyze and provide detailed descriptions of the room condition. Additionally, classify the room as fully furnished, semi-furnished, or unfurnished."""
    #     prompt = """Describe this interior quality, room condition and furnishing and rate them"""
    #     prompt = """Describe this image using human sentiments"""
    prompt = """Name the furniture items present in the image and rate its quality"""
    st.title("Image Analysis")
    image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if image is not None:
        with st.spinner("Uploading Image.."):
            uploaded_image = Image.open(image)
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            st.success("Image Uploaded Successfully!", icon="✅")

    if st.button("Submit", help="Generate Response"):
        with st.spinner("Generating Response.."):
            enc_image = model.encode_image(uploaded_image).to(device)
            st.subheader("Response:")
            description = model.answer_question(enc_image, prompt, tokenizer)
            st.write(description)
            rating = get_rating(description)
            st.subheader(f"Rating: {rating}/10")


if __name__ == "__main__":
    main()