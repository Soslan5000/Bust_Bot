from telebot.types import ReplyKeyboardMarkup


menu_btn = "В меню"
links_btn = "/links"
men_btn = "/menu"
pts_btn = "/pts"
about_btn = "/about"
continue_btn =  "далее"
back_btn = "назад"
na_accaut_btn = "на аккаунте"
s_chelom_btn = "с бустером"


markup_with_menu = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_menu.row(menu_btn)

markup_with_comands = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_comands.row(pts_btn, about_btn)
markup_with_comands.row(links_btn, men_btn)

markup_with_next = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_next.row(continue_btn,menu_btn)


markup_with_back = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_back.row(back_btn,continue_btn,menu_btn)


markup_with_bust = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_bust.row(na_accaut_btn,s_chelom_btn)
markup_with_bust.row(back_btn,continue_btn,menu_btn)

markup_for_ancket_etap = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_ancket_etap.row(back_btn, menu_btn)