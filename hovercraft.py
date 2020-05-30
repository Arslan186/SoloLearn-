vessel =10
release_vessel = 2000000
sale = 3000000
insurance = 1000000

#сумма вложений
result_expenses = vessel * release_vessel + insurance

#количество проданых
sale_vessel = int(input())

#сумма проданных
summ_sale = sale * sale_vessel

#доход
income = summ_sale - result_expenses

if result_expenses < summ_sale:
    print("Profit")
elif result_expenses > summ_sale:
    print("Loss")
elif result_expenses == summ_sale:
    print("Broke Even")

