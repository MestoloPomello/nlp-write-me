from sklearn.decomposition import LatentDirichletAllocation

def classify_sections(X, labels):
    # Classificazione con LDA
    lda = LatentDirichletAllocation(n_components=3, random_state=42)
    lda.fit(X)
    
    # Assegna una categoria a ciascun cluster
    classifications = lda.transform(X)
    return classifications

