from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import clean_text

def calculate_match(resume_text, job_text):
    resume_text = clean_text(resume_text)
    job_text = clean_text(job_text)

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_text])

    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)
