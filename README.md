## **Структура модулей проекта**
### **1. Инициализация и запуск**
-	Автоматическое определение конфигурации оборудования игрока;
-	Выбор и подстройка графических и звуковых настроек (разрешение, качество текстур, объём эффектов);
-	Подключение игровых контроллеров и возможность перепривязки управления;
-	Подключение к онлайн-функциям (для обмена результатами, обновлений и достижений).

------------

### **2. Титульный экран и меню**
-	Главное меню с возможностями: начать новую игру, загрузить сохранение, открыть галерею, просмотреть обучение, настройки;
-	Анимации и музыка фона, подчёркивающие стиль игры;
-	Привязка к системам сохранений;
-	Отображение прогресса игрока и сложности пройденной кампании.

------------

### **3. Пролог / обучение**
-	Обработка базового передвижения, прыжков, уклонений;
-	Управление камерой (автоматическая и ручная);
-	Визуализация главного героя и интерфейса (полосы здоровья, энергии и стиля);
-	Интерактивное обучение боевой системе (лёгкие и тяжёлые атаки, комбо, переключение оружия, пушки);
-	Система ранга за бой (D - SSS), основанная на разнообразии атак и урона;
-	Введение в сюжет через кат-сцены на движке игры (реализация системы сценариев);
-	Начальный бой с мини-боссом (демонстрация босса, поле с ограждением, поведение ИИ, интро-бой).

------------

### **4. Структура миссий**
-	Загрузка уровней (городские руины, замки, адские порталы);
-	Система навигации и перехода между зонами;
-	Управление событиями уровня (скрипты, кат-сцены, спавн врагов);
-	Механика "закрытых арен" — бой до зачистки врагов;
-	Прогресс миссий (таймер, цель, отображение задачи);
-	Оценка игрока по завершению уровня: время, стиль, урон, предметы.

------------

### **5. Боевая система**
-	Динамическая система комбо и рейтинг боя (мгновенный пересчёт оценки);
-	Механика "свободы": возможность менять оружие и стиль боя на лету;
-	Разнообразие оружия: холодное, дальнобойное, специальные навыки;
-	Поддержка различных стилей боя (Trickster, Swordmaster, Gunslinger, Royal Guard);
-	Визуальные и аудио-эффекты атак, отражающих стиль игрока.

------------

### **6. Враги и боссы**
-	Система ИИ врагов: патрулирование, обнаружение игрока, реакция на атаки;
-	Поведение уникальных врагов и боссов;
-	Система анимации с фазами (боссы с 2-3 фазами боя);
-	Скрипты кат-сцен до/после боёв с боссами.

------------

### **7. Галерея и коллекционные элементы**
-	Просмотр разблокированных кат-сцен и концепт-артов;
-	Трофеи/ачивки за выполнение заданий (высокий стиль, прохождение без урона и т.д.);
-	Система секретов: скрытые комнаты, испытания, бонусы;
-	Коллекционные предметы (синие осколки, секретные миссии).

------------

### **8. Прокачка и улучшения**
-	Магазин у NPC (вызов через портал/меню);
-	Очки стиля и красные сферы как внутриигровая валюта;
-	Прокачка умений, разблокировка новых атак и комбо;
-	Улучшение здоровья, энергии дьявола и других параметров.

------------

### **9. Оптимизация и локализация**	
-	Перевод интерфейса, субтитров, диалогов на другие языки;
-	Адаптация под различные разрешения экрана и платформы;
-	Работа с производительностью и отладка: профилирование боёв, загрузки уровней;
-	Поддержка геймпада, клавиатуры и мыши.

------------

### **10. Интеграция со Steam (Поддержка Steam SDK)**
-	Авторизация и профиль игрока:
-	Система достижений:
-	Сохранения в облаке:
-	Обновления и публикация в Steam:
-	Steam Overlay и внутриигровой интерфейс:
-	Статистика и лидеры:
