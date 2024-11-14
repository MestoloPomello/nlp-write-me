from sklearn.decomposition import LatentDirichletAllocation
from results_handler import get_random_state


def classify_sections(X, labels):
    # LDA classification
    lda = LatentDirichletAllocation(
        n_components=3,
        random_state=get_random_state()
    )
    lda.fit(X)

    # Assign a category to each cluster
    classifications = lda.transform(X)
    return classifications
