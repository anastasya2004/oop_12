class AirTicket:

    def __init__(self, string):
        info = string.split(';')
        self.passenger_name = info[0]
        self._from = info[1]
        self.to = info[2]
        self.date_time = info[3]
        self.flight = info[4]
        self.seat = info[5]
        self._class = info[6]
        self.gate = info[7]

    def __repr__(self):
        output = (f'|{self.passenger_name.ljust(16, " ")}|{self._from.ljust(4, " ")}|'
                  f'{self.to.ljust(3, " ")}|{self.date_time.ljust(16, " ")}|{self.flight.ljust(20, " ")}|'
                  f'{self.seat.ljust(4, " ")}|{self._class.ljust(3, " ")}|{self.gate.ljust(4, " ")}')
        return output


class Load:
    data = []

    @classmethod
    def write(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            for i in f.readlines()[1:]:
                passenger = AirTicket(i.strip())
                Load.data.append(passenger)