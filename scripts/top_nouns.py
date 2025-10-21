from itertools import tee
import stanza
import pandas as pd
import sys
import os

language = sys.argv[1] if len(sys.argv) > 1 else "lt"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
freq_csv = os.path.join(BASE_DIR, "results", "freq_list.csv")
df = pd.read_csv(freq_csv)

# Pobranie jezyka litewskiego
stanza.download(language)

# Ladowanie modelu 
nlp = stanza.Pipeline(language)

# analiza 2000 najczestszch slow 
words_top = df["word"][:2000].tolist() # wez 2000 slow najczestszych 
text_sample = " ".join(words_top)
doc = nlp(text_sample)

nouns = []
for sentence in doc.sentences:
    for word in sentence.words:
        if word.upos == "NOUN":  # tylko rzeczowniki
            nouns.append(word.text)

print("Rzeczowniki:", nouns[:55])
# Zapisz do pliku
with open(os.path.join(BASE_DIR, "results", "top_nouns.txt"), "w", encoding='utf-8') as f:
    for noun in nouns[:55]:
        f.write(f"{noun}\n")