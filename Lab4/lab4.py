import hashlib
import time

def generate_hash(pin):
    """
    Генерує MD5 хеш для заданого PIN-коду
    
    Args:
        pin: PIN-код у вигляді рядка
    
    Returns:
        MD5 хеш у вигляді рядка
    """
    return hashlib.md5(pin.encode()).hexdigest()


def crack_pin_hash(hash_string):
    """
    Зламує MD5 хеш 5-значного PIN-коду
    
    Args:
        hash_string: MD5 хеш PIN-коду у вигляді рядка
    
    Returns:
        PIN-код у вигляді рядка або None
    """
    print("🔍 Починаємо перебір PIN-кодів...")
    start_time = time.time()
    
    for pin in range(100000):
        pin_str = f"{pin:05d}"
        pin_hash = hashlib.md5(pin_str.encode()).hexdigest()
        
        # Показуємо прогрес кожні 10000 спроб
        if pin % 10000 == 0:
            print(f"   Перевірено {pin:05d} варіантів...")
        
        if pin_hash == hash_string:
            end_time = time.time()
            elapsed = end_time - start_time
            print(f"✅ Знайдено за {elapsed:.2f} секунд!")
            print(f"   Перевірено {pin + 1} варіантів")
            return pin_str
    
    return None


def validate_pin(pin):
    """
    Перевіряє, чи є PIN-код коректним (5 цифр)
    
    Args:
        pin: PIN-код для перевірки
    
    Returns:
        True якщо валідний, False інакше
    """
    return len(pin) == 5 and pin.isdigit()


def validate_hash(hash_string):
    """
    Перевіряє, чи є хеш коректним MD5 (32 символи, hex)
    
    Args:
        hash_string: хеш для перевірки
    
    Returns:
        True якщо валідний, False інакше
    """
    if len(hash_string) != 32:
        return False
    try:
        int(hash_string, 16)  # Перевіряємо, чи це hex-рядок
        return True
    except ValueError:
        return False


def print_menu():
    """Виводить головне меню"""
    print("\n" + "="*50)
    print("🔐 ПРОГРАМА ДЛЯ РОБОТИ З MD5 ХЕШАМИ PIN-КОДІВ")
    print("="*50)
    print("1. 🔒 Згенерувати хеш з PIN-коду")
    print("2. 🔓 Зламати хеш (отримати PIN-код)")
    print("3. ❌ Вийти")
    print("="*50)


def option_generate_hash():
    """Опція 1: Генерування хешу"""
    print("\n📝 ГЕНЕРУВАННЯ MD5 ХЕШУ")
    print("-" * 50)
    
    pin = input("Введіть 5-значний PIN-код: ").strip()
    
    if not validate_pin(pin):
        print("❌ Помилка! PIN-код повинен складатися з 5 цифр.")
        return
    
    hash_result = generate_hash(pin)
    print(f"\n✅ Результат:")
    print(f"   PIN-код: {pin}")
    print(f"   MD5 хеш: {hash_result}")
    print(f"\n💡 Цей хеш можна використати для тестування злому!")


def option_crack_hash():
    """Опція 2: Злом хешу"""
    print("\n🔓 ЗЛОМ MD5 ХЕШУ")
    print("-" * 50)
    
    hash_input = input("Введіть MD5 хеш для злому: ").strip().lower()
    
    if not validate_hash(hash_input):
        print("❌ Помилка! Хеш повинен бути 32-символьним hex-рядком.")
        return
    
    print()
    result = crack_pin_hash(hash_input)
    
    if result:
        print(f"\n🎉 УСПІХ! Знайдено PIN-код: {result}")
        print(f"\n📊 Перевірка:")
        print(f"   Оригінальний хеш: {hash_input}")
        print(f"   Хеш від {result}:   {generate_hash(result)}")
    else:
        print("\n❌ PIN-код не знайдено. Можливо, це не хеш 5-значного PIN-коду.")


def main():
    """Головна функція програми"""
    print("👋 Ласкаво просимо!")
    
    while True:
        print_menu()
        choice = input("\nВиберіть опцію (1-3): ").strip()
        
        if choice == "1":
            option_generate_hash()
        elif choice == "2":
            option_crack_hash()
        elif choice == "3":
            print("\n👋 До побачення! Будьте обережні з паролями!")
            break
        else:
            print("\n❌ Невірний вибір. Будь ласка, виберіть 1, 2 або 3.")
        
        # Пауза перед наступною ітерацією
        input("\nНатисніть Enter для продовження...")


if __name__ == "__main__":
    main()
