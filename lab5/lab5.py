def encode(text):
    """
    Кодує текст за допомогою коду Хеммінга (триплікація бітів)
    """
    result = ""
    
    for char in text:
        # Конвертуємо символ в ASCII значення
        ascii_value = ord(char)
        
        # Конвертуємо ASCII в 8-бітне двійкове число
        binary = format(ascii_value, '08b')
        
        # Триплюємо кожен біт
        tripled = ''.join(bit * 3 for bit in binary)
        
        result += tripled
    
    return result


def decode(encoded_text):
    """
    Декодує текст, закодований кодом Хеммінга, та виправляє помилки
    """
    # Розбиваємо на групи по 3 символи
    groups = [encoded_text[i:i+3] for i in range(0, len(encoded_text), 3)]
    
    # Виправляємо помилки (беремо найчастіший біт)
    corrected_bits = ""
    for group in groups:
        # Рахуємо кількість 0 та 1
        zeros = group.count('0')
        ones = group.count('1')
        
        # Беремо той біт, якого більше
        corrected_bits += '0' if zeros > ones else '1'
    
    # Розбиваємо на байти (по 8 біт)
    result = ""
    for i in range(0, len(corrected_bits), 8):
        byte = corrected_bits[i:i+8]
        
        # Конвертуємо байт в десяткове число (ASCII)
        ascii_value = int(byte, 2)
        
        # Конвертуємо ASCII в символ
        result += chr(ascii_value)
    
    return result


def main():
    """
    Головна функція для взаємодії з користувачем
    """
    print("=" * 60)
    print("Програма кодування/декодування за допомогою коду Хеммінга")
    print("=" * 60)
    
    while True:
        print("\nВиберіть дію:")
        print("1. Закодувати текст")
        print("2. Декодувати текст")
        print("3. Демонстрація (приклад з 'hey')")
        print("4. Вихід")
        
        choice = input("\nВаш вибір (1-4): ").strip()
        
        if choice == '1':
            text = input("\nВведіть текст для кодування: ")
            encoded = encode(text)
            print(f"\nВхідний текст: '{text}'")
            print(f"Закодований результат: {encoded}")
            print(f"Довжина: {len(encoded)} біт (оригінал: {len(text) * 8} біт)")
            
        elif choice == '2':
            encoded_text = input("\nВведіть закодований текст (тільки 0 і 1): ").strip()
            
            # Перевірка на коректність вводу
            if not all(c in '01' for c in encoded_text):
                print("Помилка: текст може містити тільки 0 та 1!")
                continue
            
            if len(encoded_text) % 24 != 0:
                print("Помилка: довжина тексту має бути кратна 24!")
                continue
            
            try:
                decoded = decode(encoded_text)
                print(f"\nЗакодований текст: {encoded_text}")
                print(f"Декодований результат: '{decoded}'")
            except Exception as e:
                print(f"Помилка при декодуванні: {e}")
                
        elif choice == '3':
            print("\n" + "=" * 60)
            print("ДЕМОНСТРАЦІЯ з текстом 'hey'")
            print("=" * 60)
            
            demo_text = "hey"
            print(f"\n1. Вхідний текст: '{demo_text}'")
            
            # Показуємо ASCII значення
            ascii_values = [ord(c) for c in demo_text]
            print(f"2. ASCII значення: {ascii_values}")
            
            # Показуємо двійкові значення
            binary_values = [format(ord(c), '08b') for c in demo_text]
            print(f"3. Двійкові значення: {binary_values}")
            
            # Кодуємо
            encoded = encode(demo_text)
            print(f"4. Закодований текст (біти потроєні):")
            
            # Виводимо по символах для наочності
            for i, char in enumerate(demo_text):
                start = i * 24
                end = start + 24
                print(f"   '{char}': {encoded[start:end]}")
            
            print(f"\n5. Повний закодований рядок:")
            print(f"   {encoded}")
            
            # Імітуємо помилку
            encoded_with_error = list(encoded)
            encoded_with_error[5] = '0' if encoded_with_error[5] == '1' else '1'
            encoded_with_error = ''.join(encoded_with_error)
            
            print(f"\n6. Вносимо помилку на позиції 5:")
            print(f"   {encoded_with_error}")
            print(f"   Змінено: позиція 5 ({encoded[5]} -> {encoded_with_error[5]})")
            
            # Декодуємо з виправленням
            decoded = decode(encoded_with_error)
            print(f"\n7. Декодований текст (помилку виправлено): '{decoded}'")
            
            if decoded == demo_text:
                print("   ✓ Успішно! Текст відновлено коректно.")
            else:
                print("   ✗ Помилка відновлення.")
                
        elif choice == '4':
            print("\nДякуємо за використання програми!")
            break
            
        else:
            print("\nНевірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
