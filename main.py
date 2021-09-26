from src.api_requests.group_request import GroupRequest
from src.utils.config import get_setting
from src.utils.csv_handler import CSV_handler
from src.utils.params_collection import ParamsCollection
from src.utils.result_printer import ResultPrinter

if __name__ == '__main__':

    settings = "settings.ini"
    token = get_setting(settings, 'Settings', 'token')
    base_url = get_setting(settings, 'Settings', 'base_url')
    output_folder = get_setting(settings, 'Settings', 'output_folder')

    if not base_url:
        base_url = "https://api-ip.fssp.gov.ru/api/v1.0/"

    if not token:
        token = input("Enter api key: ")

    if not output_folder:
        output_folder = "out"

    while True:
        filename = input("Enter csv file name: ").strip()
        csv_data = CSV_handler(filename)
        try:
            csv_data.process_csv()
            break
        except FileNotFoundError:
            print("File {filename} not found".format(filename))

    rows = csv_data.get_rows()

    params_collection = ParamsCollection(input_array=rows)
    params_collection.process_input()
    params = params_collection.get_params()

    group_req = GroupRequest(token=token, params=params, url=base_url)
    group_req.group_request_native()
    result = group_req.get_result()

    printer = ResultPrinter(path=output_folder, data=result)
    printer.print_result()
