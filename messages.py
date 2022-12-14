message_for_links = '''Если Вам нужна помощь или Вы хотели бы уточнить дополнительную информацию о заказе, о работе бота
или просто поговорить, то можете воспользоваться следующими ссылками'''

message_for_menu = '''Вас приветствует бот для поднятия ПТС в Fortnite. Воспользуйтесь следующими командами:
/pts - рассчитать стоимость поднятия и оформить заказ
/links - ссылки для связи
/about - вся необходимая информация о работе бота и нашей работе
/menu - переход в меню бота'''

message_for_notice = '''Спасибо!!!
Заказ был направлен исполнителю.
У Вас отсутствует username, поэтому, возможно, исполнитель не сможет Вам ответить,
т.к. не получит ссылку на Ваш аккаунт\n
Пожалуйста, свяжитесь с ним для того, чтобы специалист смог приступить к бусту,
а также уточнить детали заказа

Ваше мнение важно для нас!
Оставьте, пожалуйста, отзыв, когда заказ будет выполнен'''

thanks_for_the_order = '''Спасибо!!!
Заказ был направлен исполнителю.
Он свяжется с Вами, как только увидит анкету.
Если необходимо, то для уточнения деталей можете написать ему, воспользовавшись соответствующей кнопкой под сообщением.

Ваше мнение важно для нас!
Оставьте, пожалуйста, отзыв, когда заказ будет выполнен"'''

message_for_about = '''Вас приветствует бот, который позволит Вам поднять ПТС в любимой игре Fortnite.
Расчёт происходит по следующему принципу:
1) Подсчитывается стоимость без учёта времени выполнения
   Берётся Ваш текущий ПТС и тот ПТС, до которого нужно пробустить
   Затем в диапазоне каждой тысячи ПТС ведётся расчёт по такой формуле
   Сумма = 0.1 * количество ПТС * (номер тысячи справа для каждой тысячи)
   Например, при подсчёте суммы от 1100 ПТС до 3500 ПТС расчёт будет выглядеть следующим образом
   Сумма = 0.1*(2000-1000)*2 + 0.1*(3000-2000)*3 + 0.1*(3500-1100) = 680 руб.
2) Подсчитывается минимальное и максимальное количество дней выполнения
   Минимальное количество дней = округлённое нацело(количество ПТС / 250 / 8)
   Максимальное количество дней = 2*минимальное количество дней
   Например, при подсчёте дней для буста от 1100 ПТС до 3500 ПТС расчёт будет следующий
   Минимальное количество дней = округлённое нацело((3500 - 1100) / 250 / 8) = 2 дня
   Максимальное количество дней = 2 * 2 дня = 4 дня
3) Сумма корректируется в зависимости от срока выполнения по следующей формуле
   K = -Сумму до пересчёта / минимальное количество дней
   B = 3 * Сумму до пересчёта
   Конечная сумма = K * выбранное количество дней + B
   Например, при подсчёте суммы от 1100 ПТС до 3500 ПТС расчёт будет выглядеть следующим образом
   K = -680 / 2 = -340
   B = 3 * 680 = 2040
   При выборе времени выполнения 3 дня
   Конечная сумма = -340*3 + 2040 = 1020 руб.
4) Итоговая сумма зависит также от выбора способа бустинга
   С бустером + 250 руб.
   На аккаунте + 150 руб.
   Например, при подсчёте суммы от 1100 ПТС до 3500 ПТС с бустером расчёт будет выглядеть следующим образом
   Итоговая сумма = Конечная сумма + 250 = 1020 + 250 = 1270 руб.
   
После осуществления расчёта необходимо оплатить заказ и скинуть скрин чека в чат с ботом в соответствии с инструкцией
После совершения оплаты, Ваша анкета попадёт админу в базу
Необходимо написать админу. В конце всех действий будет ссылка на его телеграмм-канал. Также её можно найти, введя команду /links
   
По всем вопросам, багам и прочим проблемам также пишите админу.'''