```markdown
# 🧠 Vérificateur Grammatical avec BERT (Fine-tuning sur CoLA)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![BERT](https://img.shields.io/badge/Modèle-BERT-orange.svg)](https://huggingface.co/bert-base-uncased)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📘 Table des Matières
- [Aperçu](#aperçu)
- [Objectif du Projet](#objectif-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Détails du Modèle](#détails-du-modèle)
- [Résultats](#résultats)
- [Technologies Utilisées](#technologies-utilisées)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)
- [Remerciements](#remerciements)

---

## 🎯 Aperçu

**BERT Grammar Checker** est une application d'intelligence artificielle basée sur **BERT (Bidirectional Encoder Representations from Transformers)**, fine-tunée sur le dataset **CoLA (Corpus of Linguistic Acceptability)**.
Elle permet de **déterminer automatiquement si une phrase en anglais est grammaticalement correcte ou non**.

Ce projet se compose de deux volets principaux :
1. **Fine-tuning du modèle BERT** sur le dataset CoLA pour la classification binaire.
2. **Application Streamlit** permettant de tester le modèle via une interface intuitive et interactive.

---

## 🚀 Objectif du Projet

Ce projet a pour but de démontrer l'efficacité du **fine-tuning** d'un modèle de langage pré-entraîné pour une tâche NLP spécifique :
> 🧩 **La détection de la grammaticalité des phrases anglaises.**

Grâce au fine-tuning sur le dataset **CoLA**, le modèle apprend à distinguer :
- ✅ les phrases **grammaticalement correctes**
- ❌ les phrases **grammaticalement incorrectes**

---

## ✨ Fonctionnalités

- 🤖 **Fine-tuning de BERT** sur CoLA pour la classification binaire
- ⚡ **Analyse instantanée** des phrases anglaises
- 🌐 **Interface web Streamlit** simple et élégante
- 📊 **Résultats clairs** avec indicateurs visuels (✅ / ❌)
- 💾 **Modèle fine-tuné prêt à l'emploi**
- 🧠 **Pipeline complet reproductible** (notebook inclus)

---

## 📁 Structure du Projet

```bash
📦 BERT_GrammaCheck/
│
├── 📁 bert_cola_finetuned/      # Modèle BERT fine-tuné et tokenizer sauvegardés
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer_config.json
│   ├── vocab.txt
│   └── special_tokens_map.json
│
├── 📁 notebook_model/
│   └── bert_cola_fine_tuning_explained.ipynb   # Notebook complet de fine-tuning
│
├── 📄 app.py                    # Application Streamlit (interface utilisateur)
├── 📄 requirements.txt          # Liste des dépendances
├── 📄 .gitignore
└── 📄 README.md                 # Documentation du projet
```

---

## ⚙️ Installation

### Prérequis

- Python 3.8+
- pip
- Git
- Jupyter Notebook (pour exécuter le notebook)
- Navigateur web (pour Streamlit)

### Étapes d'installation

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/Aymanezwikat/BERT_GrammaCheck.git
   cd BERT_GrammaCheck
   ```

2. **Créer un environnement virtuel**

   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux / Mac
   venv\Scripts\activate          # Windows
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Utilisation

### 🔹 Étape 1 : Entraînement du modèle (Fine-tuning)

Ouvre et exécute le notebook :

```bash
jupyter notebook notebook_model/bert_cola_fine_tuning_explained.ipynb
```

Le notebook contient :

1. Chargement du dataset **CoLA**
2. Prétraitement et tokenisation
3. Fine-tuning de BERT
4. Évaluation des performances
5. Sauvegarde du modèle dans `bert_cola_finetuned/`

---

### 🔹 Étape 2 : Lancement de l'application Streamlit

Une fois le modèle entraîné et sauvegardé (ou si vous utilisez le modèle déjà fourni dans `bert_cola_finetuned/`) :

```bash
streamlit run app.py
```

Puis ouvre le lien :
👉 `http://localhost:8501`

**Interface utilisateur :**

- Saisis une phrase en anglais
- Clique sur **Analyser**
- Le résultat s'affichera automatiquement :
  - ✅ *Phrase grammaticalement correcte*
  - ❌ *Phrase incorrecte grammaticalement*

---

## 🔬 Détails du Modèle

| Élément | Détail |
|----------|--------|
| **Architecture** | BERT-base-uncased |
| **Type de tâche** | Classification binaire |
| **Dataset** | CoLA (Corpus of Linguistic Acceptability) |
| **Frameworks** | PyTorch & Hugging Face Transformers |
| **Optimiseur** | AdamW |
| **Métriques** | Accuracy, F1-Score, MCC |

---

## 📊 Résultats

Le modèle fine-tuné atteint :

- **Haute précision** sur les phrases grammaticalement correctes
- **Excellente généralisation** sur les phrases non vues
- **MCC élevé**, indiquant une performance robuste même sur données déséquilibrées

Les résultats détaillés et les courbes d'apprentissage sont visibles dans le notebook d'entraînement.

---

## 🧰 Technologies Utilisées

| Technologie | Rôle |
|--------------|------|
| **Python 3.8+** | Langage principal |
| **PyTorch** | Framework d'apprentissage profond |
| **Transformers (Hugging Face)** | Implémentation BERT |
| **Streamlit** | Interface utilisateur web |
| **Pandas / NumPy** | Manipulation de données |
| **Jupyter Notebook** | Environnement interactif |
| **Datasets (Hugging Face)** | Chargement de CoLA |

---

## 🤝 Contribution

Les contributions sont encouragées !
Pour proposer une amélioration :

1. Fork le dépôt
2. Crée une nouvelle branche (`feature/ta_fonctionnalite`)
3. Commit et push tes modifications
4. Ouvre une Pull Request 🎯

**Idées de contributions possibles :**

- Support pour d'autres langues
- Amélioration de l'UI Streamlit
- Visualisation des scores de confiance
- Optimisation de la vitesse d'inférence

---

## 📜 Licence

Ce projet est distribué sous la licence **MIT**.
Consulte le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 📧 Contact

👤 **Ayman Ezwikat**  
🔗 GitHub : [@Aymanezwikat](https://github.com/Aymanezwikat)  
💡 Projet : [BERT_GrammaCheck](https://github.com/Aymanezwikat/BERT_GrammaCheck)

---

## 🙏 Remerciements

- [Hugging Face](https://huggingface.co/) – pour la bibliothèque Transformers
- [Dataset CoLA](https://nyu-mll.github.io/CoLA/) – corpus linguistique d'acceptabilité
- [Streamlit](https://streamlit.io/) – framework web interactif
- [Devlin et al., 2018](https://arxiv.org/abs/1810.04805) – auteurs de BERT

---

<div align="center">
<sub>🚀 Développé avec ❤️ par Ayman Ezwikat — 2025</sub>
</div>
```