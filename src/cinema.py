from .helpers import generate_id
from .ticket import Ticket, TicketFabrica
from .user import User, UserFabrica
from .movie import Movie, MovieFabrica


class CinemaTicketSystem(UserFabrica, MovieFabrica, TicketFabrica):
    ...
