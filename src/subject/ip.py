class ExeProc():

    def __init__(self, type, number):
        self.type = type
        self.exe_number = number

    def to_string(self):
        return f'{{"type": {self.type}, "params": {{"number": "{self.exe_number}"}}}}'

    def get_ip(self):
        return {"type": self.type, "params": {"number": self.exe_number}}