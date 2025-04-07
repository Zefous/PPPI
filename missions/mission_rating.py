def calculate_mission_rating(time_taken, damage_taken, style_points):
    rank = "D"
    if style_points > 5000:
        rank = "S"
    if time_taken < 300 and damage_taken < 50:
        rank = "SS"
    if time_taken < 200 and damage_taken == 0:
        rank = "SSS"
    return rank

def display_mission_summary(stats):
    print("Завершение уровня:")
    print(f"Время: {stats['time']} сек.")
    print(f"Урон: {stats['damage']}")
    print(f"Стиль: {stats['style_points']} очков")
    print(f"Ранг: {calculate_mission_rating(stats['time'], stats['damage'], stats['style_points'])}")