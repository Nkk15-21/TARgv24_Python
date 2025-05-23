﻿while True:
        print("\nДобро пожаловать на парковку!")
        print("1. Введите деньги или выберите оплату картой")
        print("2. Укажите желаемую продолжительность парковки (в часах)")
        
        try:
            n = float(input("Введите сумму денег: "))
            s = 5.0  # Цена парковки за час
            t = int(input("Введите количество часов парковки: "))
            S = t * s
        except ValueError:
            print("Ошибка ввода. Попробуйте снова.")
            continue

        if n < S:
            print("Недостаточно средств. Ошибка!")
            continue

        print(f"Общая стоимость: {S:.2f}")
        
        YES = input("Оплата произведена успешно? (да/нет): ").strip().lower()
        if YES != "да":
            print("Ошибка оплаты! Попробуйте снова.")
            continue

        print(f"Оплата успешно произведена! Ваша парковка началась на {t} часов.")
        
        # Имитация прохода времени
        for i in range(t):
            print(f"Проходит время... {i + 1} час(ов)")
        
        print("\nАвтомат сообщает: Время парковки закончилось.")
        dop = input("Хотите продлить парковку? (да/нет): ").strip().lower()
        
        if dop == "да":
            print("Переход к продлению времени парковки.")
            continue
        else:
            print("Парковочное место освобождено. Спасибо за использование!")
            break

