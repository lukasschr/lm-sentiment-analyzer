from pathlib import Path
import yaml


def load_config(file_path: Path) -> dict:
    """Loads a YAML configuration file and returns it as a dictionary.

    Args:
        file_path (Path): The path to the YAML file.

    Returns:
        dict: The loaded configuration as a dictionary.
    """
    with open(file_path, "r", encoding="utf-8") as yaml_file:
        return yaml.safe_load(yaml_file)


CONFIG = load_config(Path("config.yml"))