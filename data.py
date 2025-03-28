
class Data:

    data_for_create_order = [
        ['Яна', 'Иванова', 'Ветлужская', 'Сокольники', '+79999999999', 3, '2025-04-01', 'a', None, None],
        ['Иван', 'Борисов', 'Перекресток, 7', 'Арбатская', '89999999999', 1, '2025-09-25', '', 'BLACK', None],
        ['Ян', 'Бекмамбетов', 'Новосибирская, 25', 'Павелецкая', '80000000000', 7, '2026-01-20', 'Кататься вдесятером', 'GREY', None],
        ['Николай', 'Невозмутимый', 'Менделеева, 11', 4, '+70000000000', 6, '2026-01-20', 'Кататься вдесятером!', 'GREY', 'BLACK']
    ]
    data_for_create_order_id_courier_known = [["11", 1, 0], [None, 2, 0], ["6", 29, 0], ["1", 30, 0]]
    data_for_create_order_id_courier_unknown = [["112", 10, 0]]

    text_message_for_successful_create_courier = '{"ok":true}'
    text_message_for_create_courier_without_data_needed = '{"message": "Недостаточно данных для создания учетной записи"}'
    text_message_for_create_courier_login_busy = '{"message": "Этот логин уже используется"}'
    message_for_courier_login_without_data_needed = '{"message": "Недостаточно данных для входа"}'
    message_for_courier_login_not_found = '{"message": "Учетная запись не найдена"}'
    message_for_get_order_list_courier_not_found = '{"message": "Курьер с идентификатором {courierId} не найден"}'

