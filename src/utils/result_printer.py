import datetime
import json
import os


class ResultPrinter():

    def __init__(self, path, data):
        self.out_path = path
        self.data = data

    def print_result(self):
        timestamp = self.get_timestamp()
        self.data = json.dumps(self.data, indent=4, ensure_ascii=False)
        self.out_path = self.get_path()
        with open(f"{self.out_path}/{timestamp} out.json", "a", encoding="utf-8") as file:
            file.write(self.data)

    def get_timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    def get_path(self):
        if os.path.exists(self.out_path):
            return self.out_path
        else:
            try:
                os.mkdir(self.out_path)
            except OSError:
                print(f"Creation output folder {self.out_path} failed")
            else:
                print(f"Successfully created output folder: {self.out_path}")
                return self.out_path
