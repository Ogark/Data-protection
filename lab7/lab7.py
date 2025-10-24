import math
import time

def baby_step_giant_step(g, h, q):
    """
    Знаходить x таке, що g^x mod q = h
    Використовує алгоритм Baby-step Giant-step (Шенкса)
    
    Args:
        g: генератор
        h: результат g^x mod q
        q: просте число (модуль)
    
    Returns:
        x: секретний ключ (дискретний логарифм)
    """
    print(f"  → Обчислюємо m = ⌈√{q}⌉ = {math.isqrt(q - 1) + 1}")
    m = math.isqrt(q - 1) + 1
    
    # Baby step
    print(f"  → Baby step: створюємо таблицю g^j mod q для j = 0..{m-1}")
    baby_steps = {}
    power = 1
    for j in range(m):
        if power not in baby_steps:
            baby_steps[power] = j
        power = (power * g) % q
    print(f"  → Таблиця створена, записів: {len(baby_steps)}")
    
    # Обчислюємо g^(-m) mod q
    g_m = pow(g, m, q)
    g_m_inv = pow(g_m, q - 2, q)
    print(f"  → Giant step: g^(-{m}) mod {q} = {g_m_inv}")
    
    # Giant step
    gamma = h
    for i in range(m):
        if gamma in baby_steps:
            j = baby_steps[gamma]
            x = i * m + j
            if pow(g, x, q) == h:
                print(f"  ✓ Знайдено на ітерації {i}: x = {i}*{m} + {j} = {x}")
                return x
        gamma = (gamma * g_m_inv) % q
    
    return None


def brute_force_attack(g, h, q, max_iterations=1000000):
    """
    Проста атака перебором (для малих значень X)
    """
    print(f"  → Перебираємо значення x від 0 до {min(max_iterations, q-1)}")
    power = 1
    for x in range(min(max_iterations, q)):
        if power == h:
            print(f"  ✓ Знайдено на ітерації {x}")
            return x
        if x % 10000 == 0 and x > 0:
            print(f"    Перевірено {x} значень...")
        power = (power * g) % q
    return None


def discrete_log_attack(g, h, q):
    """
    Головна функція для атаки на ElGamal
    """
    # Для малих Q використовуємо brute force
    if q < 1000000:
        print("📌 Використовується метод brute force (Q < 1,000,000)")
        result = brute_force_attack(g, h, q)
        if result is not None:
            return result
    
    # Для більших Q використовуємо Baby-step Giant-step
    print("📌 Використовується алгоритм Baby-step Giant-step")
    return baby_step_giant_step(g, h, q)


def verify_result(g, x, h, q):
    """
    Перевіряє правильність знайденого ключа
    """
    result = pow(g, x, q)
    print("\n" + "="*60)
    print("ПЕРЕВІРКА РЕЗУЛЬТАТУ:")
    print(f"  G^X mod Q = {g}^{x} mod {q} = {result}")
    print(f"  H (очікуване) = {h}")
    if result == h:
        print("  ✅ УСПІХ! Секретний ключ знайдено правильно!")
    else:
        print("  ❌ ПОМИЛКА! Результат не співпадає!")
    print("="*60)
    return result == h


def run_example(example_num, g, q, x_real):
    """
    Запускає приклад з заданими параметрами
    """
    print("\n" + "="*60)
    print(f"ПРИКЛАД {example_num}")
    print("="*60)
    
    # Alice генерує публічний ключ
    h = pow(g, x_real, q)
    print(f"📤 Alice генерує ключі:")
    print(f"   Секретний ключ X = {x_real} (тримає в таємниці)")
    print(f"   Обчислює H = G^X mod Q = {g}^{x_real} mod {q} = {h}")
    print(f"   Публікує: G={g}, H={h}, Q={q}")
    
    print(f"\n🎯 Атака: шукаємо X таке, що {g}^X mod {q} = {h}")
    
    start_time = time.time()
    x_found = discrete_log_attack(g, h, q)
    elapsed_time = time.time() - start_time
    
    if x_found is not None:
        print(f"\n💡 ЗНАЙДЕНИЙ СЕКРЕТНИЙ КЛЮЧ: X = {x_found}")
        print(f"⏱️  Час виконання: {elapsed_time:.4f} секунд")
        verify_result(g, x_found, h, q)
    else:
        print("\n❌ Не вдалося знайти секретний ключ")


def interactive_mode():
    """
    Інтерактивний режим для введення власних даних
    """
    print("\n" + "="*60)
    print("ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("="*60)
    print("Введіть компоненти публічного ключа ElGamal:")
    
    try:
        g = int(input("  G (генератор): "))
        h = int(input("  H (публічний ключ, G^X mod Q): "))
        q = int(input("  Q (просте число): "))
        
        # Базова валідація
        if g <= 0 or h <= 0 or q <= 0:
            print("❌ Помилка: всі значення повинні бути додатними")
            return
        
        if g >= q or h >= q:
            print("❌ Помилка: G та H повинні бути менші за Q")
            return
        
        print(f"\n🎯 Атака: шукаємо X таке, що {g}^X mod {q} = {h}")
        
        start_time = time.time()
        x_found = discrete_log_attack(g, h, q)
        elapsed_time = time.time() - start_time
        
        if x_found is not None:
            print(f"\n💡 ЗНАЙДЕНИЙ СЕКРЕТНИЙ КЛЮЧ: X = {x_found}")
            print(f"⏱️  Час виконання: {elapsed_time:.4f} секунд")
            verify_result(g, x_found, h, q)
        else:
            print("\n❌ Не вдалося знайти секретний ключ")
            
    except ValueError:
        print("❌ Помилка: введіть коректні цілі числа")
    except KeyboardInterrupt:
        print("\n\n⚠️  Перервано користувачем")


# Головне меню
if __name__ == "__main__":
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "АТАКА НА ШИФРУВАННЯ ElGamal" + " "*20 + "║")
    print("║" + " "*10 + "Discrete Logarithm Attack" + " "*23 + "║")
    print("╚" + "="*58 + "╝")
    
    while True:
        print("\n" + "-"*60)
        print("МЕНЮ:")
        print("  1 - Приклад 1 (малі значення, Q=23)")
        print("  2 - Приклад 2 (середні значення, Q=1009)")
        print("  3 - Приклад 3 (великі значення, Q=10007)")
        print("  4 - Ввести власні дані")
        print("  5 - Запустити всі приклади")
        print("  0 - Вихід")
        print("-"*60)
        
        choice = input("Ваш вибір: ").strip()
        
        if choice == "1":
            run_example(1, g=5, q=23, x_real=7)
        
        elif choice == "2":
            run_example(2, g=2, q=1009, x_real=123)
        
        elif choice == "3":
            run_example(3, g=3, q=10007, x_real=456)
        
        elif choice == "4":
            interactive_mode()
        
        elif choice == "5":
            run_example(1, g=5, q=23, x_real=7)
            run_example(2, g=2, q=1009, x_real=123)
            run_example(3, g=3, q=10007, x_real=456)
        
        elif choice == "0":
            print("\n👋 До побачення!")
            break
        
        else:
            print("❌ Невірний вибір. Спробуйте ще раз.")
        
        input("\nНатисніть Enter для продовження...")
        print("\n" * 2)  # Очищення екрану
