import re
import sys
from collections import Counter


def count_words(text):
    words = re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?", text.lower())
    return Counter(words)


def main():
    text = sys.stdin.read()
    if not text.strip():
        text = input("请输入一段文字：")

    word_counts = count_words(text)
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
