import random

# Функция для подсчета суммы карт
def calculate_total(cards):
    total = sum(cards)
    if 11 in cards and total > 21:
        total -= 10
    return total
while True:
    start = input('Нажмите Enter что бы начать, для выхода введите ext: \n')
    start = start.lower()
    if start != 'ext':
        # Создаем колоду карт
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        player_cards = []
        dealer_cards = []
        
        # перемешали колоду
        random.shuffle(deck)
        
        # Раздаем по две карты игроку и дилеру
        for _ in range(2):
            player_cards.append(deck.pop())
            dealer_cards.append(deck.pop())

        # Печатаем карты игрока и дилера
        print("Ваши карты:", player_cards)
        print("Карта дилера:", dealer_cards[0])

        # Цикл для хода игрока
        while True:
            choice = input("Хотите взять еще карту? (да/нет): ")
            if choice.lower() == "да":
                player_cards.append(deck.pop())
                print("Ваши карты:", player_cards)
            else:
                break

        # Ход дилера
        while calculate_total(dealer_cards) < 17:
            dealer_cards.append(deck.pop())

        # Печатаем карты дилера
        print("Карты дилера:", dealer_cards)

        # Определяем победителя
        player_total = calculate_total(player_cards)
        dealer_total = calculate_total(dealer_cards)

        if player_total == dealer_total:
            print("Ничья, суммы ваших карт и карт дилера равны.")
        elif player_total > 21:
            print("Вы проиграли, сумма ваших карт больше 21.")
        elif dealer_total > 21:
            print("Вы выиграли, у дилера сумма карт больше 21.")
        elif player_total > dealer_total:
            print("Вы выиграли, ваша сумма карт больше суммы карт дилера.")
        elif player_total < dealer_total:
            print("Вы проиграли, сумма ваших карт меньше суммы карт дилера.")
    else:
        break