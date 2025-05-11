class MissionRating:
    """Класс для расчёта и отображения рейтинга игрока за миссию."""

    def calculate(self, time_taken: int, damage_taken: int, style_points: int) -> str:
        """
        Вычисляет ранг игрока.

        :param time_taken: Время прохождения.
        :param damage_taken: Полученный урон.
        :param style_points: Очки стиля.
        :return: Строка с рангом (D, S, SS, SSS).
        """
        if style_points > 5000 and damage_taken == 0 and time_taken < 200:
            return "SSS"
        elif style_points > 4000 and time_taken < 300:
            return "SS"
        elif style_points > 3000:
            return "S"
        return "D"

    def display_summary(self, stats: dict):
        """
        Отображает результаты миссии.

        :param stats: Словарь с параметрами миссии.
        """
        rank = self.calculate(stats['time'], stats['damage'], stats['style_points'])
        print("Завершение миссии:")
        print(f"- Время: {stats['time']} сек.")
        print(f"- Урон: {stats['damage']}")
        print(f"- Стиль: {stats['style_points']} очков")
        print(f"- Ранг: {rank}")
