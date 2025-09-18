text = input("Enter a String: ").strip().lower()
vowels = ["a", "e", "i", "o", "u"]

num = 0
for ch in text:
    if ch in vowels:
        num += 1

print(num)
