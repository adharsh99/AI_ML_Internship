import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_model():

    texts = [
        "python sql django fastapi git rest api",
        "python sql pandas numpy excel power bi",
        "python machine learning scikit-learn numpy pandas git",
        "python html css javascript react django git",
        "python machine learning deep learning git fastapi"
    ]

    labels = [
        "Python Developer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Full Stack Developer",
        "AI Engineer"
    ]

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()

    model.fit(X, labels)

    os.makedirs(
        "models",
        exist_ok=True
    )

    with open(
        "models/job_matching_model.pkl",
        "wb"
    ) as file:

        pickle.dump(
            {
                "model": model,
                "vectorizer": vectorizer
            },
            file
        )

    return "Model trained successfully."


def predict_job_role(skills):

    with open(
        "models/job_matching_model.pkl",
        "rb"
    ) as file:

        saved_model = pickle.load(file)

    model = saved_model["model"]

    vectorizer = saved_model["vectorizer"]

    text = " ".join(skills)

    X = vectorizer.transform([text])

    prediction = model.predict(X)

    return prediction[0]