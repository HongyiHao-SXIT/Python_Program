sentence = input("Enter a sentence: ").lower().split()

freq = {}

for ch in sentence:
    if ch.isalpha:
        freq[ch] = freq.get(ch, 0) + 1

for k in sorted(freq):
    print(f"{k}: {freq[k]}")
