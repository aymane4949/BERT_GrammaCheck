# ===============================================================
# 🧠 Application Streamlit : Vérificateur grammatical avec BERT
# ===============================================================
# Auteur  : [Ton Nom]
# Projet  : Fine-tuning de BERT sur CoLA (Corpus of Linguistic Acceptability)
# Objectif :
# Ce projet vise à effectuer le fine-tuning du modèle BERT sur le jeu de données
# CoLA afin de construire un vérificateur grammatical automatique.
# L'application Streamlit permet de tester le modèle obtenu après fine-tuning
# en analysant des phrases anglaises pour déterminer leur grammaticalité.
# ===============================================================

import torch
from transformers import BertTokenizer, BertForSequenceClassification
import streamlit as st
from PIL import Image

# ---------------------------------------------------------------
# ⚙️ 1. Chargement du modèle et du tokenizer
# ---------------------------------------------------------------
@st.cache_resource
def load_model():
    """
    Charge le modèle et le tokenizer BERT obtenus après fine-tuning
    depuis le dossier ./bert_cola_finetuned/
    """
    model_path = "./bert_cola_finetuned/"
    model = BertForSequenceClassification.from_pretrained(model_path)
    tokenizer = BertTokenizer.from_pretrained(model_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    return model, tokenizer, device

model, tokenizer, device = load_model()

# ---------------------------------------------------------------
# 🧩 2. Fonction de prédiction
# ---------------------------------------------------------------
def predict_sentence(sentence: str) -> str:
    """
    Prend une phrase en entrée et renvoie si elle est grammaticalement correcte ou non.
    """
    inputs = tokenizer.encode_plus(
        sentence,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors="pt"
    )
    input_ids = inputs['input_ids'].to(device)
    attention_mask = inputs['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()

    return "✅ Phrase grammaticalement correcte" if prediction == 1 else "❌ Phrase incorrecte grammaticalement"

# ---------------------------------------------------------------
# 🎨 3. Interface utilisateur Streamlit
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Vérificateur grammatical BERT",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Vérificateur grammatical avec BERT")
st.write(
    """
    Ce modèle repose sur un **fine-tuning de BERT** réalisé à partir du dataset  
    **CoLA (Corpus of Linguistic Acceptability)**.  
    Il détermine si une phrase en anglais est grammaticalement correcte ou non.
    """
)

# (Optionnel) Image d'en-tête
# image = Image.open("bert_logo.png")
# st.image(image, caption="BERT - Fine-tuned on CoLA", use_container_width=True)

st.markdown("---")

# Champ de texte utilisateur
sentence = st.text_area("✍️ Entrez une phrase en anglais :", height=120)

# Bouton d'analyse
if st.button("Analyser"):
    if sentence.strip() == "":
        st.warning("Veuillez entrer une phrase avant d'analyser.")
    else:
        with st.spinner("Analyse en cours..."):
            result = predict_sentence(sentence)
        if "✅" in result:
            st.success(result)
        else:
            st.error(result)

# Ligne de séparation
st.markdown("---")
st.caption("Projet Fine-tuning de BERT sur CoLA — Interface Streamlit © 2025")
