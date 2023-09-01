'''
Задание 6
Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

summa = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(cash: float) -> None:
    global summa
    global count
    summa += cash
    count += 1
    if count % 3 == 0:
        summa = summa + percent_add * summa
        print("начислены проценты в размере: ", percent_add * summa)

def take_bank(cash: float) -> None:
    global summa
    global count
    summa -= cash
    count += 1

    if cash*percent_take < 30:
        summa -= 30
        print("списаны проценты за cash: ", 30)
    elif cash*percent_take > 600:
        summa -= 600
        print("списаны проценты за cash: ", 600)
    else:
        summa -= cash * percent_take
        print("списаны проценты за cash: ", cash * percent_take)
    if count % 3 == 0:
        summa = summa + percent_add * summa
        print("начислены проценты в размере: ", percent_add * summa)


def exit_bank():
    print("Рады вас видеть снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:

            return cash


while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 -выйти\n")

    if action == '1':
        if summa > 5_000_000:
            summa = summa - summa * percent_tax
            print ("списан налог на богатство: ", summa * percent_tax)
        cash = check_bank()
        if cash < summa:
            take_bank(cash)
        else:
            print("no money\n")
        if summa > 5_000_000:
            summa = summa - summa * percent_tax
            print ("списан налог на богатство: ", summa * percent_tax)
        print("Баланс = ", summa)
    elif action == '2':
        add_bank(check_bank())
        if summa > 5_000_000:
            summa = summa - summa * percent_tax
            print ("списан налог на богатство: ", summa * percent_tax)
        print("Баланс = ", summa)
    elif action == '3':
        print("Баланс = ", summa)
    else:
        exit_bank()