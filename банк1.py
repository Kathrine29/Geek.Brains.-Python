proceed = int(input('Введите сумму выручки: '))
payoff = int(input('Введите сумму издержки: '))

if proceed > payoff:
    profitability = proceed - payoff
    rent = profitability / proceed
    print(f'Отлично! Рентабельность: {profitability}')
    worker = int(input('Введите количество людей, работающих здесь: '))
    print(f"{profitability / worker} на одного работающего человека")
elif proceed == payoff:
    print("Нужно постараться!")
else:
    print("Удачи!")
