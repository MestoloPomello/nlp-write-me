import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF, TruncatedSVD
from results_handler import full_output
from stages.evaluation import compute_coherence_score, compute_topic_diversity


def run_topic_modeling(df):
    # These can be ran only once - uncomment
    # import nltk
    # nltk.download("punkt")
    # nltk.download("stopwords")
    # nltk.download('wordnet')

    # Preprocess email bodies
    df["body"] = df["body"].apply(preprocess_text)

    # Convert text in a Bag-Of-Words matrix (or TF-IDF)
    vectorizer = TfidfVectorizer(
        max_features=1000,
        stop_words='english',
        # min_df=5,   # To be valid, a term has to appear in at least 5 docs
        # max_df=0.7,  # To be valid, a term mustn't appear in less than 70% of docs
        # norm='l2'
    )
    X = vectorizer.fit_transform(df["body"])
    
    # TODO - Capire se si può usare
    # svd = TruncatedSVD(n_components=100, random_state=42)
    # X = svd.fit_transform(X)

    num_topics = 5

    # FOR REPORT: LDA gave way worse results

    # NMF (Non-negative Matrix Factorization) (test alternative to LDA)
    nmf = NMF(
        n_components=num_topics,
        random_state=42,
        # alpha_W=0.1,  # TODO - non va un cazzo
        # alpha_H=0.1,
        # l1_ratio=0.5
    )
    nmf.fit(X)

    # Evaluation part: Coherence Score with Cosine Similarity
    terms = vectorizer.get_feature_names_out()
    coherence_score = compute_coherence_score(nmf, terms, top_n=10)
    full_output(stage="Evaluation", text=f"Coherence Score: {coherence_score:.4f}", newline=True)

    # Evaluation part: diversity between topics
    diversity_score = compute_topic_diversity(nmf, terms, top_n=10)
    full_output(stage="Evaluation", text=f"Topic Diversity: {diversity_score:.4f}", newline=True)

    # Evaluation part: reconstruction error (low = best)
    # 17/3 - result with full fraud dataset looks like shit (50.2019)
    full_output(stage="Evaluation", text=f"Reconstruction Error: {nmf.reconstruction_err_:.4f}", newline=True)

    # Show the main terms for each topic
    full_output(stage="Topic Modeling", text="=== Main terms for each topic ===", newline=True)
    terms = vectorizer.get_feature_names_out()
    top_terms = [[]] * num_topics # Keep track of top terms for output purposes
    for i, topic in enumerate(nmf.components_):
        top_terms[i] = [terms[i] for i in topic.argsort()[-10:]]  # First 10 words per topic
        full_output(stage="Topic Modeling", text=f"Topic {i}: {', '.join(top_terms[i])}", newline=True)

    # Assign the dominant topic to each email (the text and not the topic number)
    topic_assignments = nmf.transform(X).argmax(axis=1)
    # print("topic_assugnments", type(topic_assignments))
    df["topic"] = topic_assignments
    
    # Get the topic-related text using it as index from top_terms array
    df["topic"] = df["topic"].apply(lambda x: ";".join(top_terms[x]))

    # Count the topics distribution
    topic_counts = df["topic"].value_counts()

    full_output(stage="Topic Modeling", text="=== Topics distribution ===", newline=True)
    for topic, count in topic_counts.items():
        full_output(stage="Topic Modeling", text=f"Topic {topic}: {count} email", newline=True)

    return df


def preprocess_text(textList):
    text = " ".join(textList)
    text = re.sub(r'[^\w\s.]', '', text)  # Remove all non-alphabetic characters besides periods
    text = text.lower()
    tokens = text.split()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return " ".join(tokens)