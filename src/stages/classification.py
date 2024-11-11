from sklearn.decomposition import LatentDirichletAllocation

def classify_sections(X, labels):
    # LDA classification
    lda = LatentDirichletAllocation(n_components=3, random_state=42)
    lda.fit(X)
    
    # Assign a category to each cluster
    classifications = lda.transform(X)
    return classifications

