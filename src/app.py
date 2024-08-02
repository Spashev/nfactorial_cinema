from .cinema import CinemaTicketSystem


def start():
    print("""Здравствуйте, у вас есть следующие доступные функции:
    1. Добавить новый фильм;
    2. Показать все доступные фильмы;
    3. Добавить нового пользователя;
    4. Купить билет;
    5. Отменить покупку билета;""")

    cinema = CinemaTicketSystem()
    while True:
        option = input("Введите номер 1-5: ")
        match option:
            case '1':
                movie_name = input("Введите название фильма: ")
                if movie_name == '':
                    print('Название не должно быть пустым.')
                movie = cinema.addMovie(movie_name)
                print(f"Новый фильм добавлен: {movie}")
            case '2':
                cinema.showAllMovies()
            case '3':
                user_name = input("Введите имя пользователя: ")
                if user_name == '':
                    print('Имя пользователя не должно быть пустым.')
                user = cinema.addUser(user_name)
                print(f"Новый пользователя добавлен: {user}")
            case '4':
                cinema.showAllUsers()
                user_uuid = input("Введите id пользователя: ")
                cinema.showAllMovies()
                movie_uuid = input("Введите id фильма: ")
                ticket = cinema.buyTicket(user_uuid, movie_uuid)
                print(f"Билет был куплен: {ticket}")
            case '5':
                cinema.showAllTickets()
                ticket_uuid = input("Введите id билета для отмены: ")
                status = "успешно" if cinema.cancelTicket(ticket_uuid) else "неудачно"
                print(f"Статус отмены билета: {status.upper()}")
            case _:
                print('Invalid input.')
