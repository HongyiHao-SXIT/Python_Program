text = input("Enter a string: ").strip()
is_palindrome = True
for i in range(len(text)//2):
    if text[i] != text[-(i+1)]:
        is_palindrome = False
        break

print("✅ It's a palindrome!" if is_palindrome else "❌ Not a palindrome.")
