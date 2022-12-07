import telebot
from config import *
from messages import *
from inline_kb import *
from kb import *
from user_class import User
from function import *
from anceta import getRegData


bot = telebot.TeleBot(token)

user_dict = {}



@bot.message_handler(commands=["start"])
def welcome(message):
    try:
        bot.send_message(message.chat.id,
                         message_for_menu,
                         reply_markup=markup_with_comands)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)


@bot.message_handler(commands=["links"])
def send_links(message):
    try:
        bot.send_message(message.chat.id,
                         message_for_links,
                         reply_markup=kb_for_links)
        msg = bot.send_message(message.chat.id,
                               'Для возврата нажмите "В меню"',
                               reply_markup=markup_with_menu)
        bot.register_next_step_handler(msg,in_menu)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

def in_menu(message):
    try:
        bot.send_message(message.chat.id,
                             message_for_menu,
                         reply_markup=markup_with_comands)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)



@bot.message_handler(commands=["about"])
def send_about(message):
    try:
        bot.send_message(message.chat.id,
                         message_for_about)
        msg = bot.send_message(message.chat.id,
                               'Для возврата нажмите "В меню"',
                               reply_markup=markup_with_menu)
        bot.register_next_step_handler(msg,in_menu)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

def in_menu(message):
    try:
        bot.send_message(message.chat.id,
                             message_for_menu,
                         reply_markup=markup_with_comands)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

@bot.message_handler(commands=["menu"])
def in_menu(message):
    try:
        bot.send_message(message.chat.id,
                             message_for_menu,
                         reply_markup=markup_with_comands)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

@bot.message_handler(commands=["pts"])
def first_etap(message):
    try:
        user_dict[message.chat.id] = User()
        msg = bot.send_message(message.chat.id,
                                "Введите ваше количество птс",
                               reply_markup=markup_with_next)
        bot.register_next_step_handler(msg,second_etap)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)


def second_etap(message):
    try:
        user = user_dict[message.chat.id]
        if message.text == menu_btn:
            bot.send_message(message.chat.id,
                             message_for_menu,
                             reply_markup=markup_with_comands)
        else:
            if message.text != continue_btn:
                user.initial_pts = int(message.text)
            msg = bot.send_message(message.chat.id,
                                "Какое количество птс вам нужно?",
                               reply_markup=markup_with_back)
            bot.register_next_step_handler(msg,third_etap)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)


def third_etap(message):
    try:
        user = user_dict[message.chat.id]
        if message.text == menu_btn:
            bot.send_message(message.chat.id,
                             message_for_menu,
                             reply_markup=markup_with_comands)
        elif message.text == back_btn:
            msg = bot.send_message(message.chat.id,
                                   "Введите ваше количество птс",
                                   reply_markup=markup_with_next)
            bot.register_next_step_handler(msg, second_etap)
        else:
            if message.text != continue_btn:
                user.final_pts = int(message.text)
                if user.final_pts > user.initial_pts:
                    user.first_sum = first_calculation_pts(user.initial_pts, user.final_pts)
                    user.min_days, user.max_days = max_min_time(user.initial_pts, user.final_pts)
            kb_with_days = create_kb(user.min_days, user.max_days)
            msg = bot.send_message(message.chat.id,
                                   "Выберите время выполнения заказа",
                                   reply_markup=kb_with_days)
            bot.register_next_step_handler(msg,fourth_etap)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

def fourth_etap(message):
    try:
        user = user_dict[message.chat.id]
        if message.text == menu_btn:
            bot.send_message(message.chat.id,
                             message_for_menu,
                             reply_markup=markup_with_comands)
        elif message.text == back_btn:
            msg = bot.send_message(message.chat.id,
                                   "Какое количество птс вам нужно?",
                                   reply_markup=markup_with_back)
            bot.register_next_step_handler(msg, third_etap)
        elif message.text == continue_btn:
            msg = bot.send_message(message.chat.id,
                                   "Выберите способ выполнения",
                                   reply_markup=markup_with_bust)
            bot.register_next_step_handler(msg, fifth_etap)
        elif int(message.text) < user.min_days or int(message.text) > user.max_days:
            if user.initial_pts < user.final_pts:
                user.first_sum = first_calculation_pts(user.initial_pts, user.final_pts)
                user.min_days, user.max_days = max_min_time(user.initial_pts, user.final_pts)
            kb_with_days = create_kb(user.min_days, user.max_days)
            msg = bot.send_message(message.chat.id,
                                   "Выберите время выполнения заказа",
                                   reply_markup=kb_with_days)
            bot.register_next_step_handler(msg, fourth_etap)
        else:
            user.lead_time = int(message.text)
            msg = bot.send_message(message.chat.id,
                                   "Выберите способ выполнения",
                                   reply_markup=markup_with_bust)
            bot.register_next_step_handler(msg, fifth_etap)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

def fifth_etap(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if message.text == na_accaut_btn or message.text == s_chelom_btn:
            user.method = message.text
        user.final_sum = end_calculation_pts(user.lead_time, user.min_days, user.first_sum, user.method)
        if message.text == menu_btn:
            bot.send_message(message.chat.id,
                             message_for_menu,
                             reply_markup=markup_with_comands)
        elif message.text == back_btn:
            kb_with_days = create_kb(user.min_days, user.max_days)
            msg = bot.send_message(message.chat.id,
                                   "Выберите время выполнения заказа",
                                   reply_markup=kb_with_days)
            bot.register_next_step_handler(msg, fourth_etap)
        else:
            bot.send_message(chat_id,
                             getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                             parse_mode="Markdown",
                             reply_markup=markup_for_ancket_etap)
            msg = bot.send_message(chat_id,
                                   'Необходимо приложить скриншот или документ с оплатой\n'
                                   'чтобы мы могли приступить к выполнению заказа\n'
                                   'Номер карты (тинькоф):\n'
                                   '4377720007501802\n'
                                   'Номер карты (сбер):\n'
                                   '2202202308730070\n'
                                   'ФИО: Павел Олегович Романов',
                                   reply_markup=markup_for_ancket_etap)
            bot.register_next_step_handler(msg, ready_step)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

def ready_step(message):
    try:
        chat_id = message.chat.id
        to_chat_id = TG_ANKETS_CHANNEL_ID
        user = user_dict[chat_id]
        if message.text == menu_btn:
            bot.send_message(message.chat.id,
                             message_for_menu,
                             reply_markup=markup_with_comands)
        elif message.text == back_btn:
            msg = bot.send_message(message.chat.id,
                                   "Выберите способ выполнения",
                                   reply_markup=markup_with_bust)
            bot.register_next_step_handler(msg, fifth_etap)
        else:
            if message.content_type == 'photo' or message.content_type == 'document':
                if message.from_user.username is None:
                    bot.send_message(to_chat_id,
                                     getRegData(user, 'Анкета пользователя ', message.from_user.first_name),
                                     parse_mode="Markdown")
                    bot.send_message(chat_id,
                                     message_for_notice,
                                     reply_markup=keyboard_for_end)
                    msg = bot.send_message(message.chat.id,
                                           'Для возврата нажмите "В меню"',
                                           reply_markup=markup_with_menu)
                else:
                    bot.send_message(to_chat_id,
                                     getRegData(user, 'Анкета пользователя @', message.from_user.username),
                                     parse_mode="Markdown")
                    bot.send_message(chat_id,
                                     thanks_for_the_order,
                                     reply_markup=keyboard_for_end)
                    msg = bot.send_message(message.chat.id,
                                           'Для возврата нажмите "В меню"',
                                           reply_markup=markup_with_menu)
                bot.forward_message(to_chat_id, chat_id, message.id)
            else:
                msg = bot.send_message(chat_id,
                                       'Необходимо приложить скриншот или документ с оплатой\n'
                                       'чтобы мы могли приступить к выполнению заказа\n'
                                       'Номер карты (тинькоф):\n'
                                       '4377720007501802\n'
                                       'Номер карты (сбер):\n'
                                       '2202202308730070\n'
                                       'ФИО: Павел Олегович Романов',
                                       reply_markup=markup_for_ancket_etap)
                bot.register_next_step_handler(msg, ready_step)

    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)

@bot.message_handler(content_types="text")
def in_menu(message):
    try:
        bot.send_message(message.chat.id,
                         message_for_menu,
                         reply_markup=markup_with_comands)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)


if __name__ == "__main__":
    bot.polling(non_stop=True)



