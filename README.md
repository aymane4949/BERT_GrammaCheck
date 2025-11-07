# 🧠 Vérificateur de Grammaire BERT

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![BERT](https://img.shields.io/badge/Modèle-BERT-orange.svg)](https://huggingface.co/bert-base-uncased)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Table des Matières
- [Aperçu](#aperçu)
- [Objectif du Projet](#objectif-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Détails du Modèle](#détails-du-modèle)
- [Technologies Utilisées](#technologies-utilisées)
- [Résultats](#résultats)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

## 🎯 Aperçu

**BERT_GrammaCheck** est une application intelligente basée sur le modèle **BERT** (Bidirectional Encoder Representations from Transformers) qui permet de **vérifier la grammaticalité de phrases en anglais**.

Ce projet comprend deux grandes parties :
1. Le **fine-tuning du modèle BERT** sur le jeu de données **CoLA (Corpus of Linguistic Acceptability)**
2. Une **application Streamlit** pour tester le modèle fine-tuné de manière interactive

## 🚀 Objectif du Projet

L'objectif de ce projet est de démontrer l'utilisation du **fine-tuning** d'un modèle de langage pré-entraîné (BERT) pour une tâche de **classification binaire** :

> **Déterminer si une phrase en anglais est grammaticalement correcte ou incorrecte.**

Le système utilise le dataset **CoLA** pour entraîner un classificateur binaire capable d'évaluer l'acceptabilité linguistique des phrases anglaises.

## ✨ Fonctionnalités

- 🤖 **Modèle BERT Fine-tuné** : Entraîné spécifiquement sur le dataset CoLA pour l'évaluation grammaticale
- 🌐 **Interface Web Interactive** : Application Streamlit conviviale pour des tests en temps réel
- ⚡ **Inférence Rapide** : Prédictions instantanées de grammaticalité avec scores de confiance
- 📊 **Classification Binaire** : Identification précise des phrases correctes/incorrectes
- 💾 **Modèle Pré-entraîné** : Modèle fine-tuné prêt à l'emploi inclus dans le dépôt
- 🔄 **Entraînement Reproductible** : Notebook Jupyter complet pour l'entraînement et l'évaluation
- 📈 **Métriques de Performance** : Évaluation détaillée avec accuracy, F1-score et MCC

## 📁 Structure du Projet

Voici la structure détaillée du dossier :

```
📦 BERT_GrammaCheck/
│
├── 📁 model_save/                          # Modèle BERT fine-tuné et tokenizer sauvegardés
│   ├── config.json                         # Configuration du modèle
│   ├── model.safetensors                   # Poids du modèle
│   ├── special_tokens_map.json             # Mapping des tokens spéciaux
│   ├── tokenizer_config.json               # Configuration du tokenizer
│   └── vocab.txt                           # Fichier vocabulaire
│
├── 📁 notebook_model/
│   └── bert_cola_fine_tuning.ipynb         # Notebook de fine-tuning du modèle BERT
│
├── 📁 venv/                                # Environnement virtuel (non suivi par Git)
│
├── 📄 app.py                               # Application Streamlit pour tester le modèle
├── 📄 requirements.txt                     # Dépendances Python nécessaires
├── 📄 .gitignore                           # Fichiers et dossiers à ignorer par Git
└── 📄 README.md                            # Documentation complète du projet
```

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git
- Environnement virtuel (recommandé)

### Instructions d'Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Aymanezwikat/BERT_GrammaCheck.git
   cd BERT_GrammaCheck
   ```

2. **Créer un environnement virtuel**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Utilisation

### Partie 1 : Fine-tuning du Modèle BERT

Le notebook `bert_cola_fine_tuning.ipynb` contient le pipeline complet :

1. **Chargement du dataset CoLA**
2. **Préparation et prétraitement des données**
3. **Fine-tuning du modèle BERT**
4. **Évaluation des performances**
5. **Sauvegarde du modèle** dans `model_save/`

Pour exécuter le notebook :

```bash
jupyter notebook notebook_model/bert_cola_fine_tuning.ipynb
```

Le modèle final classe une phrase :
- ✅ **Correcte grammaticalement**
- ❌ **Incorrecte grammaticalement**

### Partie 2 : Application Streamlit

L'application `app.py` permet de tester le modèle via une interface web interactive.

**Lancer l'application :**

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://localhost:8501`

**Utilisation de l'interface :**

1. Saisissez une phrase en anglais dans le champ de texte
2. Cliquez sur le bouton de vérification
3. Consultez le résultat :
   - ✅ **Grammaticalement Correcte** : La phrase est bien formée
   - ❌ **Grammaticalement Incorrecte** : La phrase contient des erreurs grammaticales

## 🔬 Détails du Modèle

### Architecture

- **Modèle de Base** : `bert-base-uncased`
- **Tâche** : Classification Binaire de Séquences
- **Dataset** : CoLA (Corpus of Linguistic Acceptability)
- **Framework** : Hugging Face Transformers + PyTorch

### Pipeline d'Entraînement

1. **Chargement des Données** : Dataset CoLA avec labels de grammaticalité (0/1)
2. **Tokenisation** : Utilisation du tokenizer BERT avec padding et troncature
3. **Fine-tuning** : Ajout d'une tête de classification binaire sur BERT pré-entraîné
4. **Optimisation** : Entraînement avec AdamW et learning rate scheduling
5. **Évaluation** : Calcul des métriques sur l'ensemble de test
6. **Sauvegarde** : Export du modèle et du tokenizer

### Métriques de Performance

Le modèle est évalué selon des métriques NLP standard :
- **Accuracy** : Exactitude globale des prédictions
- **F1-Score** : Moyenne harmonique de la précision et du recall
- **Matthews Correlation Coefficient (MCC)** : Métrique de qualité pour classification binaire

## 🛠️ Technologies Utilisées

| Technologie | Version | Utilisation |
|------------|---------|-------------|
| **Python** | 3.8+ | Langage de programmation principal |
| **PyTorch** | Latest | Framework de deep learning |
| **Transformers** | Hugging Face | Implémentation du modèle BERT |
| **Streamlit** | Latest | Framework d'application web |
| **Pandas** | Latest | Manipulation de données |
| **NumPy** | Latest | Calculs numériques |
| **Jupyter** | Latest | Développement interactif |
| **Datasets** | Hugging Face | Chargement du dataset CoLA |

## 📊 Résultats

Le modèle BERT fine-tuné atteint des performances solides sur l'ensemble de test CoLA :
- Capacité à identifier les patterns grammaticaux complexes
- Détection efficace des erreurs de syntaxe
- Haute précision dans la classification binaire

Les métriques détaillées, les courbes d'apprentissage et l'analyse complète sont disponibles dans le notebook d'entraînement `bert_cola_fine_tuning.ipynb`.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request. 

### Pour contribuer :

1. Forkez le dépôt
2. Créez votre branche de fonctionnalité (`git checkout -b feature/NouvelleFonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/NouvelleFonctionnalite`)
5. Ouvrez une Pull Request

### Idées de contributions :

- Support multilingue (français, espagnol, etc.)
- Amélioration de l'interface Streamlit
- Ajout de nouvelles métriques d'évaluation
- Optimisation des performances
- Documentation supplémentaire

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📧 Contact

**Ayman Ezwikat**

- GitHub : [@Aymanezwikat](https://github.com/Aymanezwikat)
- Projet : [BERT_GrammaCheck](https://github.com/Aymanezwikat/BERT_GrammaCheck)

---

## 🙏 Remerciements

- [Hugging Face](https://huggingface.co/) pour la bibliothèque Transformers et l'écosystème NLP
- Les créateurs du [Dataset CoLA](https://nyu-mll.github.io/CoLA/) (Corpus of Linguistic Acceptability)
- Les auteurs du [Paper BERT](https://arxiv.org/abs/1810.04805) : Devlin et al. (2018)
- La communauté Streamlit pour le framework d'applications web

---

## 📚 Ressources Supplémentaires

- [Documentation BERT](https://huggingface.co/docs/transformers/model_doc/bert)
- [Guide de Fine-tuning](https://huggingface.co/docs/transformers/training)
- [Dataset CoLA](https://nyu-mll.github.io/CoLA/)
- [Documentation Streamlit](https://docs.streamlit.io/)

---

<div align="center">
  <sub>Développé avec ❤️ en utilisant BERT et Streamlit | 2025</sub>
</div>