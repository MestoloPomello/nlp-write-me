from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from results_handler import get_random_state, full_output


stage_name = "Clustering"


def cluster_sections(emails):
    # Remove english stop words
    vectorizer = TfidfVectorizer(stop_words='english')
    sections = ["greeting", "body", "closing"]
    results = {}

    for section in sections:
        section_texts = [email[section] for email in emails if email[section]]

        if section_texts:
            # Generates sparse matrix:
            #   row = email,
            #   col = term,
            #   value = weight of term
            X = vectorizer.fit_transform(section_texts)

            # Clustering with K-Means
            num_clusters = 3  # E.g., for greetings, body, closures
            kmeans = KMeans(
                n_clusters=num_clusters,
                random_state=get_random_state()
            )
            labels = kmeans.fit_predict(X)

            results[section] = {
                "labels": labels,
                "vectorized_data": X,
                "top_terms": extract_top_terms(kmeans, vectorizer)
            }

    # full_output(stage="Clustering", text=("Labels: " + "".join(str(labels))))
    # full_output(stage=stage_name, text="Results: ")
    # full_output(stage=stage_name, text=results)

    return results


def extract_top_terms(kmeans, vectorizer, top_n=5):
    terms = vectorizer.get_feature_names_out()
    top_terms = []

    for i, centroid in enumerate(kmeans.cluster_centers_):
        terms_with_weights = sorted(
            zip(terms, centroid), key=lambda x: x[1], reverse=True
        )
        top_terms.append([term for term, weight in terms_with_weights[:top_n]])

    return top_terms
