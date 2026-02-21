from preprocessing import preprocess_text
from relation_extraction import extract_relations_regex as extract_relations

def run_nlp_pipeline(text):

    processed = preprocess_text(text)
    relations = extract_relations(text)

    return {
        "cleaned_sentences": processed,
        "relations": relations
    }

# 🔹 Test
if __name__ == "__main__":
    text = "Google is investing in AI"
    result = run_nlp_pipeline(text)
    print(result)

