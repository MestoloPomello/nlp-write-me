from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_sections(emails):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(emails)
    
    # Clustering with K-Means
    num_clusters = 3  # E.g., for greetings, body, closures
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(X)
    
    return labels, X

