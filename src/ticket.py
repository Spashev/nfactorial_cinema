from .helpers import generate_id


class Ticket:
    """
    class Ticket
    private attribute tickets
    methods:
        buyTicket
        cancelTicket
        showAllTickets
    """
    __tickets = {}

    def buyTicket(self, user: str, movie: str) -> str:
        ticket_id = generate_id()
        self.__tickets[ticket_id] = {
            'user': user,
            'movie': movie
        }
        return ticket_id

    def cancelTicket(self, ticket_id) -> bool:
        try:
            self.__tickets.pop(ticket_id)
            return True
        except Exception:
            return False

    def showAllTickets(self):
        print("# Вывод билетов:")
        for ticket_id in self.__tickets.keys():
            print(f"# {ticket_id}")
