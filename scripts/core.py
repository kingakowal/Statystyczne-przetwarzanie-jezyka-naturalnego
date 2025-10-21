import re 
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx 
from itertools import tee
import sys
import os

language = sys.argv[1] if len(sys.argv) > 1 else "litewski"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
corpus_path = os.path.join(BASE_DIR, "corpus", f"{language}.txt")
results_dir = os.path.join(BASE_DIR, "results")
os.makedirs(results_dir, exist_ok=True)

with open(corpus_path, "r", encoding='utf-8') as file:
    text = file.read().lower()

# Cleaning
text = re.sub(r'[^a-ž]', ' ', text)
text = re.sub(r'\s+', ' ', text).strip()

# Core - graph
def grams(text):
    # Zachowanie granic - .
    sentences = re.split(r'[.!?]+', text)
    all_bigrams = []

    for sent in sentences:
        sent = re.sub(r'[^a-ząčęėįšųūž\s]', ' ', sent.lower())  # lista pojedynczych zmian
        sent = re.sub(r'\s+', ' ', sent).strip() 
        words = [w for w in sent.split()] # zamiana slow na liste
        a, b = tee(words)
        next(b, None)
        all_bigrams.extend(zip(a, b))
    return all_bigrams 

bigrams = Counter(grams(text))
top_bigrams = bigrams.most_common(50)

G = nx.Graph()
for (a, b), f in top_bigrams:
    G.add_edge(a, b, weight=f)

for (word_a, word_b), freq in top_bigrams:
        print(f"| {word_a} | {word_b} | {freq} |")

plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=2, iterations=50)

nx.draw(G, pos, 
            with_labels=True,
            font_size=9,
            font_weight='bold',
            node_color='lightblue',
            node_size=800,
            edge_color='gray',
            alpha=0.7,
            width=1.5)
    
plt.title("Rdzeń języka litewskiego - graf współwystępowania słów", 
            fontsize=14, pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(results_dir, 'language_core.png'), dpi=300, bbox_inches='tight')
#plt.show()