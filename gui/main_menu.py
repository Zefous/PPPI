def display_main_menu():
    print("1. Новая игра")
    print("2. Загрузить игру")
    print("3. Галерея")
    print("4. Обучение")
    print("5. Настройки")
    print("Выберите опцию...")

def handle_menu_input(choice):
    if choice == 1:
        start_new_game()
    elif choice == 2:
        load_game()
    elif choice == 3:
        open_gallery()
    elif choice == 5:
        open_settings()
