## Auteurs
# Votre Nom - https://www.linkedin.com/in/abdelwahedkabouri - Remplacez ceci par votre lien LinkedIn


# Job Matcher

Job Matcher est une application web qui permet aux utilisateurs de comparer un CV avec une offre d'emploi et d'obtenir une évaluation de leur adéquation. Cette application utilise des techniques d'extraction de texte et de traitement du langage naturel pour déterminer si un candidat est un bon match pour une position donnée.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribution](#contribution)
- [License](#license)

## Fonctionnalités

- Téléchargez votre CV au format PDF ou DOCX.
- Téléchargez une offre d'emploi au format PDF ou TXT.
- Recevez une évaluation du match entre votre CV et l'offre d'emploi.
- Interface utilisateur simple et intuitive.

## Technologies utilisées

- Flask : pour le framework web
- PyMuPDF : pour l'extraction de texte à partir de fichiers PDF
- python-docx : pour l'extraction de texte à partir de fichiers DOCX
- HTML/CSS : pour le frontend
- JavaScript : pour le traitement des formulaires et les requêtes API

## Installation

Pour exécuter cette application, vous devez avoir Python installé sur votre machine. Suivez les étapes ci-dessous pour installer et configurer le projet.

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/kabouri/job_matcher.git
   cd job_matcher

## Installez les dépendances :

pip install -r requirements.txt


## Utilisation
# Exécutez l'application :

python app/main.py

# Ouvrez votre navigateur et accédez à http://127.0.0.1:5000/static/index.html.

# Téléchargez votre CV et l'offre d'emploi, puis cliquez sur Check Match pour voir les résultats.


## Structure du projet

job_matcher/
│
├── app/
│   ├── main.py                # Fichier principal de l'application
│   ├── recommender.py         # Fichier pour la logique de correspondance
│   ├── __init__.py            # Fichier d'initialisation du package
│   └── uploads/               # Dossier pour stocker les fichiers téléchargés
│
├── static/
│   └── index.html             # Page HTML pour l'interface utilisateur
│
├── requirements.txt           # Dépendances du projet
└── README.md                  # Documentation du projet


## Licence

# Ce projet est sous la licence MIT - consultez le fichier LICENSE pour plus de détails.


### Instructions

1. **Copiez** le texte ci-dessus.
2. **Ouvrez** votre éditeur de texte ou IDE.
3. **Créez un fichier** nommé `README.md` à la racine de votre projet.
4. **Collez** le texte copié dans ce fichier.
5. **Enregistrez** le fichier.

Si vous avez besoin d'autres informations ou d'aide supplémentaire, n'hésitez pas à demander !


