from .helpers import generate_id
from .ticket import Ticket
from .user import User
from .movie import Movie


class CinemaTicketSystem(User, Movie, Ticket): ...
