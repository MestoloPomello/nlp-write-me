from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Coherence between terms in a group (i.e. "bank" and "money") (1 = best)
# 17/3 - result with full fraud dataset doesn't look good (0.6395)
def compute_coherence_score(nmf, feature_names, top_n=10):
    topic_coherence_scores = []
    
    for topic_idx, topic in enumerate(nmf.components_):
        top_indices = topic.argsort()[-top_n:]  # Takes top-N terms
        top_terms = feature_names[top_indices]

        # Creates matrix with vectorial representations of top-N terms
        term_vectors = nmf.components_[:, top_indices]

        # Calculates the cosine similarity between words in the topic
        similarity_matrix = cosine_similarity(term_vectors)

        # Considers only the top part of the matrix in order to avoid duplicates
        mean_similarity = np.mean(similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)])
        topic_coherence_scores.append(mean_similarity)
    
    # Returns the avg between all topics' coherences
    overall_coherence = np.mean(topic_coherence_scores)
    return overall_coherence


# Diversity between different topics (1 = best)
# 17/3 - result with full fraud dataset seems good (0.9)
def compute_topic_diversity(nmf, feature_names, top_n=10):
    top_words = set()
    
    for topic in nmf.components_:
        top_words.update(feature_names[topic.argsort()[-top_n:]])

    # Diversity = unique terms between top-N against the possible total
    diversity_score = len(top_words) / (top_n * nmf.n_components)
    return diversity_score
