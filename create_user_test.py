import sender_stand_request

# Меркулов Никита, 5-я когорта - финальный проект. Инженер по тестированию плюс.
def test_get_order_by_track_number():
    # Создание нового заказа
    response = sender_stand_request.post_new_order()

    if response.status_code == 201:
        track_number = response.json()["track"]
        # Получение заказа по трек-номеру
        get_order_response = sender_stand_request.get_order_by_track_number(track_number)

        # Проверка кода ответа GET-запроса
        assert get_order_response.status_code == 200, "Order retrieval failed with status code: " + str(
            get_order_response.status_code)

        # Вывод результатов GET-запроса
        print(get_order_response.json())
        print(get_order_response.status_code)
