import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_shift_incremental_encode(text, start_shift):
    result = []
    for i, ch in enumerate(text):
        shift = start_shift + i
        idx = (ALPHABET.index(ch) + shift) % 26
        result.append(ALPHABET[idx])
    return "".join(result)

def caesar_shift_incremental_decode(text, start_shift):
    result = []
    for i, ch in enumerate(text):
        shift = start_shift + i
        idx = (ALPHABET.index(ch) - shift) % 26
        result.append(ALPHABET[idx])
    return "".join(result)

def substitution_encode(text, rotor):
    result = []
    for ch in text:
        idx = ALPHABET.index(ch)
        result.append(rotor[idx])
    return "".join(result)

def substitution_decode(text, rotor):
    result = []
    for ch in text:
        idx = rotor.index(ch)
        result.append(ALPHABET[idx])
    return "".join(result)

if __name__ == "__main__":
    mode = input().strip()       # ENCODE or DECODE
    start_shift = int(input().strip())
    rotor1 = input().strip()
    rotor2 = input().strip()
    rotor3 = input().strip()
    message = input().strip()

    if mode == "ENCODE":
        # 1) Caesar shift
        step1 = caesar_shift_incremental_encode(message, start_shift)
        # 2) три ротори
        step2 = substitution_encode(step1, rotor1)
        step3 = substitution_encode(step2, rotor2)
        step4 = substitution_encode(step3, rotor3)
        print(step4)

    elif mode == "DECODE":
        # 1) три ротори у зворотньому порядку
        step1 = substitution_decode(message, rotor3)
        step2 = substitution_decode(step1, rotor2)
        step3 = substitution_decode(step2, rotor1)
        # 2) Caesar shift у зворотному напрямку
        step4 = caesar_shift_incremental_decode(step3, start_shift)
        print(step4)
