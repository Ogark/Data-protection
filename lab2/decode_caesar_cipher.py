def decode_caesar_cipher(encoded_message):
    """
    Decodes a Caesar cipher using frequency analysis.
    
    Args:
        encoded_message: The encoded string to decode
        
    Returns:
        tuple: (decoded_message, best_shift)
    """
    # English letter frequencies (in percentages)
    english_freq = {
        'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56,
        'F': 2.17, 'G': 1.80, 'H': 5.27, 'I': 7.24, 'J': 0.14,
        'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47,
        'P': 1.91, 'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15,
        'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21, 'Y': 1.65, 'Z': 0.07
    }
    
    def shift_text(text, shift):
        """Apply shift to alphabetical characters only, preserve case."""
        result = []
        for char in text:
            if char.isalpha():
                # Determine if uppercase or lowercase
                is_upper = char.isupper()
                # Convert to uppercase for processing
                char = char.upper()
                # Apply shift
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                # Restore original case
                result.append(shifted if is_upper else shifted.lower())
            else:
                # Non-alphabetical characters remain unchanged
                result.append(char)
        return ''.join(result)
    
    def calculate_chi_squared(text):
        """Calculate chi-squared statistic for frequency analysis."""
        # Count letter frequencies in the text
        letter_counts = {}
        total_letters = 0
        
        for char in text.upper():
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1
                total_letters += 1
        
        if total_letters == 0:
            return float('inf')
        
        # Calculate chi-squared statistic
        chi_squared = 0
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            observed = letter_counts.get(letter, 0)
            expected = (english_freq[letter] / 100) * total_letters
            if expected > 0:
                chi_squared += ((observed - expected) ** 2) / expected
        
        return chi_squared
    
    # Try all possible shifts (0-25)
    best_shift = 0
    best_score = float('inf')
    
    for shift in range(26):
        decoded = shift_text(encoded_message, shift)
        score = calculate_chi_squared(decoded)
        
        if score < best_score:
            best_score = score
            best_shift = shift
    
    # Decode with the best shift
    decoded_message = shift_text(encoded_message, best_shift)
    
    return decoded_message, best_shift


# Test the decoder
if __name__ == "__main__":
    print("=" * 60)
    print("CAESAR CIPHER DECODER - FREQUENCY ANALYSIS")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        # Test 1: Simple encoded message (shift 3)
        "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj!",
        
        # Test 2: Famous quote (shift 13)
        "Gb or, be abg gb or: gung vf gur dhrfgvba.",
        
        # Test 3: Mixed case with numbers and symbols (shift 5)
        "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl 123!",
        
        # Test 4: Secret message (shift 7)
        "Aol jylhapvu vm zvtlaopun ulc pz hsdhnz wyljlklk if aol klzaybjaopvu vm zvtlaopun vsk.",
        
        # Test 5: Short message with punctuation (shift 10)
        "Rovvy, Gybvn!"
    ]
    
    for i, encoded in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Encoded: {encoded}")
        decoded, shift = decode_caesar_cipher(encoded)
        print(f"Decoded: {decoded}")
        print(f"Shift used: {shift}")
        print("-" * 60)
    
    # Interactive mode
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)
    print("\nEnter your own encoded message (or press Enter to skip):")
    user_input = input("> ")
    
    if user_input.strip():
        decoded, shift = decode_caesar_cipher(user_input)
        print(f"\nDecoded message: {decoded}")
        print(f"Shift detected: {shift}")
    else:
        print("No input provided. Exiting interactive mode.")
    
    print("\n" + "=" * 60)
    print("Decoding complete!")
    print("=" * 60)
