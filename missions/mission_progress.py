import time

mission_data = {
    "goal": "Победить босса",
    "time_limit": 600,  # секунд
}

def start_mission_timer():
    start_time = time.time()
    print("Миссия началась.")
    return start_time

def check_goal_completion(state):
    if state.get("boss_defeated"):
        print("Цель выполнена!")
        return True
    print("Цель ещё не выполнена.")
    return False