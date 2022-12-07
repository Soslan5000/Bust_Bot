from telebot.types import ReplyKeyboardMarkup

def first_calculation_pts(a0, an):
    d1 = (a0 // 1000 + 1) * 1000 - a0  # Какое кол-во ПТС будет от ПТС игрока до близжайшей тысячи вверх
    d2 = an - (an // 1000) * 1000  # Какое кол-во ПТС будет от близжайшей тысячи снизу до требуемого ПТС
    n = ((an // 1000) - (a0 // 1000 + 1))  # Количество тысяч между d1 и d2

    kn = 0.1  # коэффициент пропорциональности коэффициента пропорциональности
    s1 = d1 * (a0 // 1000 + 1) * kn  # Стоимость ПТС от ПТС игрока до близжайшей тысячи вверх
    s2 = d2 * (an // 1000 + 1) * kn  # Стоимость ПТС от близжайшей тысячи снизу до требуемого ПТС

    start = a0 // 1000 + 1  # Первая тысяча
    stop = an // 1000  # Последняя тысяча

    summ = 0
    for i in range(start, stop):
        sn = 1000 * kn * (i + 1)  # Стоимость ПТС промежуточных тысяч
        summ += sn

    end_summ = s1 + s2 + summ  # Суммарная стоимость ПТС

    return end_summ


def max_min_time(a0, an):
    ### Расчёт максимального и минимального времени
    t_min = (an - a0) / 250
    if t_min % 8 == 0:
        d_min = t_min // 8
    else:
        d_min = t_min // 8 + 1
    t_max = 2 * t_min
    if t_min % 8 == 0:
        d_max = t_max // 8
    else:
        d_max = t_max // 8 + 1
    d_max = 2 * d_min
    return int(d_min), int(d_max)


def end_calculation_pts(days, d_min, end_summ, method):
    s_min = end_summ
    s_max = 2 * end_summ

    K = -s_min / d_min
    B = 3 * s_min

    end_time_summ = K * days + B

    if method == 'с бустером':
        end_time_summ += 250
    else:
        end_time_summ += 150

    return round(end_time_summ, 3)

def create_kb(min_days, max_days):
    kb_with_days = ReplyKeyboardMarkup(resize_keyboard=True)
    count = 0
    list_with_btn = []
    for i in range(min_days, max_days+1):
        list_with_btn.append(str(i))
        count += 1
        if count >= 5:
            kb_with_days.row(list_with_btn[0], list_with_btn[1], list_with_btn[2], list_with_btn[3], list_with_btn[4])
            list_with_btn.clear()
            count = 0
    if len(list_with_btn) == 1:
        kb_with_days.row(list_with_btn[0])
    elif len(list_with_btn) == 2:
        kb_with_days.row(list_with_btn[0], list_with_btn[1])
    elif len(list_with_btn) == 3:
        kb_with_days.row(list_with_btn[0], list_with_btn[1], list_with_btn[2])
    elif len(list_with_btn) == 4:
        kb_with_days.row(list_with_btn[0], list_with_btn[1], list_with_btn[2], list_with_btn[3])
    menu_btn = "В меню"
    continue_btn = "далее"
    back_btn = "назад"
    kb_with_days.row(back_btn, continue_btn, menu_btn)
    return kb_with_days

