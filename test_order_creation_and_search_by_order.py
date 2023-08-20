import sender_stand_request


def test_order_creation_and_search_by_track():
    response = sender_stand_request.get_track()
    assert response.status_code == 201, "Ожидается статус 201, фактически имеем {}".format(response.status_code)
    track_number = response.json()["track"]

    response = sender_stand_request.get_order_by_track(track_number)

    assert response.status_code == 200, "Ожидается статус 200, фактически имеем {}".format(response.status_code)


# Антон Дмитриев, 7-я когорта - DIPLOM_Dmitriev. Инженер по тестированию плюс.
