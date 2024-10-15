from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_match(cv_text, job_text):
    documents = [cv_text, job_text]
    
    # Utiliser TF-IDF pour vectoriser le texte
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculer la similarité cosinus
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    similarity_score = similarity_matrix[0][0]

    # Définir un seuil de similarité
    threshold = 0.1  # Vous pouvez ajuster ce seuil selon vos besoins
    match = bool(similarity_score >= threshold)  # Convertir en bool standard

    return {
        'match': match,
        'similarity_score': float(similarity_score)  # Convertir en float standard
    }
