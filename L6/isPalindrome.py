def is_palindrome(text):
    text_curat = text.lower().replace(" ", "")
    return text_curat == text_curat[::-1]

try:
    input_text = input("Introdu textul: ").strip()
    if not input_text:
        raise ValueError("Nu ai introdus nimic!")

    if is_palindrome(input_text):
        print("Este palindrom!")
    else:
        print("Nu este palindrom!")

except ValueError as e:
    print(f"ERROR: {e}")