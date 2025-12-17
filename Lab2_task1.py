money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mounths = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
for i in range(10000):
    money_capital += salary
    if spend > money_capital:
        break
    money_capital -= spend
    spend += increase * spend
    mounths +=1
print("Количество месяцев, которое можно протянуть без долгов:", mounths)
