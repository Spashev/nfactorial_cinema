from .helpers import generate_id
from .ticket import TicketFabrica
from .user import UserFabrica
from .movie import MovieFabrica


class CinemaTicketSystem(UserFabrica, MovieFabrica, TicketFabrica):
    ...
