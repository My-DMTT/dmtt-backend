from datetime import datetime

import pytz


def get_current_datetime_tashkent():
    # Установка часового пояса для Ташкента
    tz_tashkent = pytz.timezone('Asia/Tashkent')

    # Получение текущего времени в заданном часовом поясе
    datetime_tashkent = datetime.now(tz_tashkent)

    return datetime_tashkent


# Вызов функции
current_datetime_tashkent = get_current_datetime_tashkent()
print(current_datetime_tashkent)
