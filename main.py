# Дан список с визитами по городам и странам.
# Напишите код, который возвращает отфильтрованный список geo_logs,
# содержащий только визиты из России."

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def geo_logs_func(list_geo):
    for visit in list(list_geo):
        if 'Россия' not in list(visit.values())[0]:
            list_geo.remove(visit)
    return list_geo

# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def unique_ids(some_dict):
    values = list(some_dict.values())
    geo_ids = []
    for value in values:
        geo_ids.extend(value)
    return list(set(geo_ids))

# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.


stats = {'facebook': 55, 'yandex': 120, 'vk': 115,
         'google': 99, 'email': 42, 'ok': 98}


def max_vol_channel(some_dict):
    inv_stats = {value: key for key, value in stats.items()}
    keys = list(inv_stats.keys())
    x = max(keys)
    return inv_stats.get(x)
