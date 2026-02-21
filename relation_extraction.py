import re

def extract_relations_regex(text):
    # Match: Capitalized subject, then some words, then capitalized object
    pattern = r"([A-Z][a-zA-Z]+) (.*?) ([A-Z][a-zA-Z]+)"
    matches = re.findall(pattern, text)

    relations = []
    for subj, verb_phrase, obj in matches:
        relations.append({
            "subject": subj,
            "relation": verb_phrase.strip(),
            "object": obj
        })
    return relations

text = "Google is investing in AI research in India."
print(extract_relations_regex(text))



