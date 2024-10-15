from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import fitz  # PyMuPDF pour extraire du texte des fichiers PDF
import docx  # Pour extraire du texte des fichiers DOCX
from app.recommender import check_match

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Dossier pour stocker les fichiers téléchargés

# Créer le dossier de téléchargement s'il n'existe pas
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/match', methods=['POST'])
def match():
    if 'cv' not in request.files or 'job' not in request.files:
        return jsonify({"error": "Missing file(s)"}), 400

    cv_file = request.files['cv']
    job_file = request.files['job']

    # Sauvegarder les fichiers téléchargés
    cv_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(cv_file.filename))
    job_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(job_file.filename))
    cv_file.save(cv_path)
    job_file.save(job_path)

    # Extraire le texte du CV et de l'offre d'emploi
    cv_text = extract_text_from_cv(cv_path)
    job_text = extract_text_from_job(job_path)

    result = check_match(cv_text, job_text)

    return jsonify(result)

def extract_text_from_cv(cv_path):
    # Extraire le texte du CV
    if cv_path.endswith('.pdf'):
        with fitz.open(cv_path) as doc:
            return "\n".join(page.get_text() for page in doc)
    elif cv_path.endswith('.docx'):
        # Pour les fichiers DOCX
        doc = docx.Document(cv_path)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    return ""

def extract_text_from_job(job_path):
    # Extraire le texte de l'offre d'emploi
    if job_path.endswith('.txt'):
        with open(job_path, 'r') as file:
            return file.read()
    elif job_path.endswith('.pdf'):
        with fitz.open(job_path) as doc:
            return "\n".join(page.get_text() for page in doc)
    return ""

if __name__ == "__main__":
    app.run(debug=True)
