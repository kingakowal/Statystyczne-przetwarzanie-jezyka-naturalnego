import re 
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

language = sys.argv[1] if len(sys.argv) > 1 else "litewski"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
corpus_path = os.path.join(BASE_DIR, "corpus", f"{language}.txt")
results_dir = os.path.join(BASE_DIR, "results")
os.makedirs(results_dir, exist_ok=True)

# Load corpus
with open(corpus_path, "r", encoding='utf-8') as file:
    text = file.read().lower()

# Cleaning
text = re.sub(r'[^a-ž]', ' ', text)
text = re.sub(r'\s+', ' ', text).strip()

words = text.split()

# Frequency list 
freq = Counter(words) 
freq_list = freq.most_common()

df = pd.DataFrame(freq_list, columns=["word", "frequency"])
df["r"] = range(1, len(df)+1)
df["r*f"] = df["r"] * df["frequency"]

df.to_csv(os.path.join(results_dir, "freq_list.csv"), index=False)

# Zipf Law 
plt.loglog(df["r"], df["frequency"], marker=".", color="black")
plt.xlabel("Ranga (r)")
plt.ylabel("Czestotliwosc (f)")
plt.title("Zipf Law")
plt.savefig(os.path.join(results_dir, 'ZipfLaw.png'))
# plt.show()

# 90% text
cum_sum = df["frequency"].cumsum()
total_sum = df["frequency"].sum()

percent = cum_sum / total_sum

all_less = percent[percent <= 0.90]
print(f"Trzeba znać {len(all_less) + 1} słów, by rozumieć 90% tekstu.")