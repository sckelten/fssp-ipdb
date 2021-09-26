import csv


class CSV_handler:

    def __init__(self, file):
        self.file = file
        self.rows = []
        self.params_array = []

    def process_csv(self):
        try:
            with open(self.file, "r", newline="") as csv_file:
                csv_data = csv.DictReader(csv_file, delimiter=';')
                for row in csv_data:
                    # self.rows.append(''.join(row))
                    self.rows.append(row)
        except FileNotFoundError:
            raise FileNotFoundError

    def get_rows(self):
        return self.rows
