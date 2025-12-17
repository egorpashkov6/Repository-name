salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for money_capital in range(10000000):
    money = money_capital
    for month in range(months):
        money += salary
        money -= spend
        spend *= (1 + increase)
        if money < 0:
            spend = 6000
            break
    if money >= 0:
        print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
        break
