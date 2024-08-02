from collections import namedtuple

from .helpers import generate_id
from .user import User
from .movie import Movie

Ticket = namedtuple('Ticket', ['id', 'user', 'movie'])


class TicketFabrica:
    __tickets = list()

    def buyTicket(self, user: User, film: Movie) -> Ticket:
        ticket = Ticket(generate_id(), user, film)
        self.__tickets.append(ticket)
        return ticket

    def cancelTicket(self, ticket: Ticket) -> bool:
        try:
            index = self.__tickets.index(ticket)
            self.__tickets.pop(index)
            return True
        except Exception:
            return False
