def space_game(text):
    print(text.count(" "))
    if text.count(" ") % 2 == 0:
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")


space_game('Привет, как дела?')
