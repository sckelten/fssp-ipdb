import configparser
import os


def create_config(path):

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "token", "")
    config.set("Settings", "base_url", "https://api-ip.fssp.gov.ru/api/v1.0/")
    config.set("Settings", "output_folder", "out")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):

    if not os.path.exists(path):
        print('Файл с настройками не был найден и был создан заново')
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):

    config = get_config(path)
    value = config.get(section, setting)
    return value
