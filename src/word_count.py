import re
from collections import Counter
import sys

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return Counter(words)

def main(file_path):
    counter = word_count(file_path)
    for word, count in counter.most_common():
        print(f"{count} {word}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
