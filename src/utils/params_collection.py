from src.subject.ip import ExeProc
from src.subject.physical import Physical

class ParamsCollection():

    def __init__(self, input_array):
        self.params = []
        self.input_array = input_array

    def process_input(self):
        for row in self.input_array:
            type = row['type']
            if type == '1':
                physical = Physical(row['type'], row['firstname'], row['secondname'], row['lastname'], row['birthdate'], row['region'])
                self.params.append(physical.get_physical())
            elif type == '3':
                exe_proc = ExeProc(row['type'], row['number'])
                self.params.append(exe_proc.get_ip())
        self.chunk_params_array()

    def chunk_params_array(self):
        self.params = [self.params[d:d + 50] for d in range(0, len(self.params), 50)]

    def get_params(self):
        return self.params