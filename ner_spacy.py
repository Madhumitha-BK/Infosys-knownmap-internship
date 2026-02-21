import re

def extract_entities_regex(text):
    # Simple pattern-based NER
    entities = []
    # Detect capitalized words as PERSON/ORG/GPE
    for match in re.finditer(r"\b[A-Z][a-z]+\b", text):
        entities.append({"text": match.group(), "label": "PROPER_NOUN"})
    return entities

text = "Google is investing in AI research in India."
print(extract_entities_regex(text))

