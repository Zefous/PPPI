def display_player_progress(progress_data):
    print(f"Уровень: {progress_data.get('level')}")
    print(f"Сложность: {progress_data.get('difficulty')}")
    print(f"Прогресс: {progress_data.get('completion')}%")