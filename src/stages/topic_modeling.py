import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


def topic_modeling(email_bodies, n_topics=5):
    # Convertire il testo in una rappresentazione Bag of Words (BoW)
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(email_bodies)

    # Applicare LDA per identificare i temi
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)

    # Ottenere le parole principali per ogni tema
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        top_terms = [feature_names[i] for i in topic.argsort()[:-11:-1]]  # Prime 10 parole
        topics.append(top_terms)

    return topics, lda, X


def assign_topics(lda, X):
    # Ottieni la distribuzione dei temi per ogni email
    topic_distributions = lda.transform(X)

    # Assegna il tema con il punteggio più alto
    assigned_topics = np.argmax(topic_distributions, axis=1)
    return assigned_topics
