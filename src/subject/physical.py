class Physical():

    def __init__(self, type, firstname, secondname, lastname, birthdate, region):
        self.type = type
        self.firstname = firstname
        self.secondname = secondname
        self.lastname = lastname
        self.birthdate = birthdate
        self.region = region

    def to_string(self):
        return f'{{"type": {self.type}, "params": ' \
               f'{{"firstname": {self.firstname}, ' \
               f'"secondname": {self.secondname}, ' \
               f'"lastname": {self.lastname}, ' \
               f'"birthdate": "{self.birthdate}", ' \
               f'"region": {self.region}}}}}'

    def get_physical(self):
        physical = {"type": self.type, "params": {"firstname": self.firstname,
                                               "lastname": self.lastname,
                                               "region": self.region}}
        if self.birthdate != '':
            physical["params"]["birthdate"] = self.birthdate
        if self.secondname != '':
            physical["params"]["secondname"] = self.secondname
        return physical
