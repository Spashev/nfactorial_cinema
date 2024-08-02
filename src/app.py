from .cinema import CinemaTicketSystem


def start():
    print("""Здравствуйте, у вас есть следующие доступные функции:
    1. Добавить новый фильм;
    2. Показать все доступные фильмы;
    3. Добавить нового пользователя;
    4. Купить билет;
    5. Отменить покупку билета;""")

    cinema = CinemaTicketSystem()

    options = {
        '1': add_movie,
        '2': show_movies,
        '3': add_user,
        '4': buy_ticket,
        '5': cancel_ticket
    }

    while True:
        option = input("Введите номер 1-5: ")
        if option in options:
            options[option](cinema)
        else:
            print('Неверный ввод. Попробуйте снова.')


def add_movie(cinema):
    movie_name = input("Введите название фильма: ").strip()
    if not movie_name:
        print('Название не должно быть пустым.')
    else:
        movie = cinema.addMovie(movie_name)
        print(f"Новый фильм добавлен: {movie}")


def show_movies(cinema):
    cinema.showAllMovies()


def add_user(cinema):
    user_name = input("Введите имя пользователя: ").strip()
    if not user_name:
        print('Имя пользователя не должно быть пустым.')
    else:
        user = cinema.addUser(user_name)
        print(f"Новый пользователь добавлен: {user}")


def buy_ticket(cinema):
    cinema.showAllUsers()
    user_uuid = input("Введите id пользователя: ").strip()
    if not user_uuid:
        print('ID пользователя не должно быть пустым.')
        return
    cinema.showAllMovies()
    movie_uuid = input("Введите id фильма: ").strip()
    if not movie_uuid:
        print('ID фильма не должно быть пустым.')
        return
    ticket = cinema.buyTicket(user_uuid, movie_uuid)
    print(f"Билет был куплен: {ticket}")


def cancel_ticket(cinema):
    cinema.showAllTickets()
    ticket_uuid = input("Введите id билета для отмены: ").strip()
    if not ticket_uuid:
        print('ID билета не должно быть пустым.')
    else:
        status = "успешно" if cinema.cancelTicket(ticket_uuid) else "неудачно"
        print(f"Статус отмены билета: {status.upper()}")
