from pathlib import Path
import yaml


def load_config(file_path:Path):
    with open(file_path, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

CONFIG = load_config("config.yml")