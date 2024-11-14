from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from results_handler import get_random_state, full_output


def cluster_sections(emails):
    # Remvoe english stop words
    vectorizer = TfidfVectorizer(stop_words='english')

    # Generates sparse matrix: row = email, col = term, value = weight of term
    X = vectorizer.fit_transform(emails)

    # Clustering with K-Means
    num_clusters = 3  # E.g., for greetings, body, closures
    kmeans = KMeans(n_clusters=num_clusters, random_state=get_random_state())
    labels = kmeans.fit_predict(X)

    full_output(stage="Clustering", text=("Labels: " + "".join(str(labels))))

    return labels, X
