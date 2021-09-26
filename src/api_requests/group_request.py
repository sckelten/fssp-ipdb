import json
import time
from urllib import request as r


class GroupRequest():

    def __init__(self, token, params, url):
        self.token = token
        self.params = params
        self.base_url = url
        self.headers = {"Content-Type": "application/json", "accept": "application/json"}
        self.task = ""
        self.result = []

    def group_request_native(self):

        for counter, chunk in enumerate(self.params):
            data = {"token": self.token, "request": chunk}
            data = json.dumps(data)
            data = data.encode()
            while True:
                req = r.Request(self.base_url + "search/group", method="POST")
                req.add_header("Content-Type", "application/json")
                req.add_header("accept", "application/json")
                res = r.urlopen(req, data=data)
                response = json.loads(res.read().decode("utf-8"))
                print(f"Chunk {int(counter) + 1} response status: {response['status']}")
                if int(response["code"]) != 429:
                    break
            if response["code"] == 0:
                self.task = response["response"]["task"]
                print(f"Chunk {counter + 1}: created task {self.task}")
                self.check_task_status()
            else:
                print(f"Chunk {counter + 1} response exception: {response['exception']}")

    def check_task_status(self):
        data = {"token": self.token, "task": self.task}
        data = json.dumps(data)
        data = data.encode()
        while True:
            time.sleep(10)
            req = r.Request(self.base_url + "status", method="GET")
            req.add_header("Content-Type", "application/json")
            req.add_header("accept", "application/json")
            res = r.urlopen(req, data=data)
            response = json.loads(res.read().decode("utf-8"))
            if (response["code"] == 0) and (response["response"]["status"] == 0):
                print(f"Task {self.task} response status: {response['status']}")
                self.get_task_result()
                break

    def get_task_result(self):
        data = {"token": self.token, "task": self.task}
        data = json.dumps(data)
        data = data.encode()
        req = r.Request(self.base_url + "result", method="GET")
        req.add_header("Content-Type", "application/json")
        req.add_header("accept", "application/json")
        res = r.urlopen(req, data=data)
        response = json.loads(res.read().decode("utf-8"))
        if response["code"] == 0:
            self.result.append(response["response"]["result"])
            print(f"Task {self.task} done")

    def get_result(self):
        return self.result