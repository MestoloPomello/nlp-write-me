import spacy


nlp = spacy.load("en_core_web_sm")


def preprocess_email(email_text):
    doc = nlp(email_text)
    return [token.lemma_ for token in doc if not token.is_stop]


def extract_entities(email_text):
    doc = nlp(email_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

