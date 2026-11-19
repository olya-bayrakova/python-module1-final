"""
Программа «План самостоятельной подготовки» (Вариант 3)
Рассчитывает суммарное время самостоятельной подготовки студента,
оценивает достижение целевого показателя в 10 часов и выводит
пошаговую таблицу накопления часов по дням

Автор: Байракова Ольга
"""

TARGET_HOURS = 10.0


def read_student_name():
    """
    Запрашивает у пользователя имя студента и проверяет, что строка не пустая
    Параметры: отсутствуют
    Возвращает: очищенную от крайних пробелов строку с именем студента
    """
    name = input("Введите имя студента: ").strip()
    while name == "":
        print("Ошибка: имя не может быть пустым")
        name = input("Введите имя студента: ").strip()
    return name


def read_days():
    """
    Запрашивает количество дней подготовки от 1 до 7 включительно
    Параметры: отсутствуют
    Возвращает: корректное количество дней в диапазоне от 1 до 7
    """
    days = int(input("Введите количество дней подготовки (от 1 до 7): "))
    while days < 1 or days > 7:
        print("Ошибка: количество дней должно быть от 1 до 7 включительно")
        days = int(input("Введите количество дней подготовки (от 1 до 7): "))
    return days


def read_daily_hours():
    """
    Запрашивает ежедневное время занятий (положительное число не более 12 часов)
    Параметры: отсутствуют
    Возвращает: корректное количество часов занятий в день
    """
    hours = float(input("Введите время занятий в день (ч, от 0 до 12): "))
    while hours <= 0 or hours > 12:
        print("Ошибка: время должно быть больше 0 и не превышать 12 часов")
        hours = float(input("Введите время занятий в день (ч, от 0 до 12): "))
    return hours

def get_goal_status(total_hours, target_hours):
    """
    Определяет текстовый результат выполнения плана подготовки
    Параметры:
    1) total_hours - суммарное запланированное время в часах
    2) target_hours - целевой объем подготовки в часах
    Возвращает: строку с оценкой достаточности времени
    """
    is_exact_target = total_hours >= target_hours and total_hours <= target_hours
    if total_hours < target_hours and not is_exact_target:
        status = "Времени недостаточно"
    elif is_exact_target:
        status = "Цель достигнута"
    else:
        status = "Есть дополнительное время"
    return status

def print_plan_report(student_name, days, daily_hours, total_hours, goal_share, status, target_hours):
    """
    Выводит отформатированный итоговый отчет и построчную таблицу по дням
    Параметры:
    1) student_name - имя студента
    2) days - количество дней подготовки
    3) daily_hours - ежедневная нагрузка в часах
    4) total_hours - суммарное время подготовки в часах
    5) goal_share - доля достижения цели (отношение суммарного времени к цели)
    6) status - итоговый вывод о достижении цели
    7) target_hours - целевой объем часов
    Возвращает: ничего
    """
    line = "-" * 60
    print()
    print(f"{'ПЛАН САМОСТОЯТЕЛЬНОЙ ПОДГОТОВКИ':^60}")
    print(line)
    print(f"{'Студент:':<32}{student_name:>28}")
    print(f"{'Количество дней:':<32}{days:>25} дн.")
    print(f"{'Время занятий в день:':<32}{daily_hours:>26.2f} ч")
    print(f"{'Суммарное время:':<32}{total_hours:>26.2f} ч")
    print(f"{'Достижение цели (10.0 ч):':<32}{goal_share:>28.1%}")
    print(f"{'Результат:':<32}{status:>28}")
    print(line)
    print(f"{'День':<15}{'Накоплено (ч)':>22}{'Процент от цели':>23}")
    print(line)

    accumulated_hours = 0.0
    for day in range(1, days + 1):
        accumulated_hours += daily_hours
        day_share = accumulated_hours / target_hours
        print(f"{day:02d}{'':<13}{accumulated_hours:>22.2f}{day_share:>23.1%}")

    print(line)


def ask_repeat():
    """
    Запрашивает у пользователя решение о повторном составлении плана
    Параметры: отсутствуют
    Возвращает: True для нового расчета ('да') или False для завершения ('нет')
    """
    answer = input("Составить новый план? (да/нет): ").strip().lower()
    while answer != "да" and answer != "нет":
        print("Пожалуйста, введите «да» или «нет».")
        answer = input("Составить новый план? (да/нет): ").strip().lower()
    return answer == "да"


def main():
    """
    Управляет основным циклом работы программы: ввод данных, расчет, вывод и повтор
    Параметры: отсутствуют
    Возвращает: ничего
    """
    is_running = True

    while is_running:
        student_name = ""
        days = 0
        daily_hours = 0.0
        total_hours = 0.0
        goal_share = 0.0

        student_name = read_student_name()
        days = read_days()
        daily_hours = read_daily_hours()

        total_hours = days * daily_hours
        goal_share = total_hours / TARGET_HOURS
        status = get_goal_status(total_hours, TARGET_HOURS)

        print_plan_report(student_name=student_name, days=days, daily_hours=daily_hours, total_hours=total_hours, goal_share=goal_share, status=status, target_hours=TARGET_HOURS)
        is_running = ask_repeat()

    print("Работа программы завершена")

main()