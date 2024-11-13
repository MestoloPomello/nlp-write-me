from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from results_handler import get_random_state

def cluster_sections(emails):
    vectorizer = TfidfVectorizer(stop_words='english') # Remvoe english stop words
    X = vectorizer.fit_transform(emails) # Generates sparse matrix X: row = email, col = term, value = weight of term
    
    # Clustering with K-Means
    num_clusters = 3  # E.g., for greetings, body, closures
    kmeans = KMeans(n_clusters=num_clusters, random_state=get_random_state())
    labels = kmeans.fit_predict(X)
    
    return labels, X

