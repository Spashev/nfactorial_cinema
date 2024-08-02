from .cinema import CinemaTicketSystem


def start():
    cinema = CinemaTicketSystem()
    movie1 = cinema.addMovie('Iron man')
    movie2 = cinema.addMovie('Hulk')
    movie3 = cinema.addMovie('Superman')
    movie4 = cinema.addMovie('Spiderman')
    cinema.showAllMovies()

    print("################################")

    user1 = cinema.addUser('Tony Stark')
    user2 = cinema.addUser('Bruce Banner')
    user3 = cinema.addUser('Clark Kent')
    user4 = cinema.addUser('Peter Parker')
    cinema.showAllUsers()

    print("################################")

    ticket1 = cinema.buyTicket(user1, movie1)
    ticket2 = cinema.buyTicket(user2, movie2)
    ticket3 = cinema.buyTicket(user3, movie3)
    ticket4 = cinema.buyTicket(user4, movie4)

    print("################################")

    cancel1 = cinema.cancelTicket(ticket1)
    cancel2 = cinema.cancelTicket('a4b3f4ed-12a5-4781-963c-5b7750702374')
    cancel3 = cinema.cancelTicket(ticket2)
    cancel4 = cinema.cancelTicket(ticket4)
    print(cancel1, cancel2, cancel3, cancel4)
