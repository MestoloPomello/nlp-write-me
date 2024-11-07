import re


# Regex - ToDo - translate in english 
greetings = r"\b(Ciao|Gentile|Egregio|Salve|Buongiorno|Buonasera)\b"
closings = r"\b(Cordiali saluti|Distinti saluti|Un caro saluto|A presto|Cordiali|Saluti)\b"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_pattern = r"\b(\+?\d{1,3})?\s?(\(?\d{1,4}\)?)\s?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b"


def extract_greetings_closings(email_text):
    greeting_match = re.search(greetings, email_text)
    closing_match = re.search(closings, email_text)
    
    greeting = greeting_match.group() if greeting_match else None
    closing = closing_match.group() if closing_match else None
    
    return greeting, closing


def extract_signature(email_text):
    # Starting from the bottom, search for the latest matches for email addresses and phone numbers
    email_matches = re.findall(email_pattern, email_text)
    phone_matches = re.findall(phone_pattern, email_text)

    if email_matches or phone_matches:
        # Consider everything following the last match as a sign
        last_contact_index = max(email_text.rfind(email) for email in email_matches) if email_matches else len(email_text)
        last_phone_index = max(email_text.rfind(phone) for phone in phone_matches) if phone_matches else len(email_text)
        signature_index = min(last_contact_index, last_phone_index)
        
        signature = email_text[signature_index:].strip()
        return signature
    return None

