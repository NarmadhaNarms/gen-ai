import spacy
nlp = spacy.load("en_core_web_sm")
review = ["This is a great movie. I really enjoye+++d it!",
           "i love 9 sac", 
           "i hate sac",
            
             "i like sac",
               "i dislike sac",
                 "i adore sac",
                   "i detest sac"]
def clean_text(text):
    doc = nlp(text)
    clean_text = []
    for i in doc:
        if i.is_punct:            continue
        if i.is_digit:            continue
        if i.is_space:            continue
        clean_text.append(i.text.lower())
    return " ".join(clean_text)
for sentence in review:
    print(clean_text(sentence))