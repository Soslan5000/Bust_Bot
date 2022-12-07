from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


kb_for_links = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text="Мой тик ток", url="https://www.tiktok.com/@cryzzzzzzzzzz")
btn2 = InlineKeyboardButton(text="группа в вк", url="https://vk.com/so3fmebust")
btn3 = InlineKeyboardButton(text="Лс", url="https://t.me/pi3daa")
kb_for_links.row(btn1)
kb_for_links.row(btn2)
kb_for_links.row(btn3)

keyboard_for_end = InlineKeyboardMarkup()
btn = InlineKeyboardButton(text='Телега оператора', url='https://t.me/pi3daa')
keyboard_for_end.add(btn)