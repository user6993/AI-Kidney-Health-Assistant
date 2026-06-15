import os

from joblib import logger
from box.exceptions import BoxValueError
import yaml
from cnnClassifier.logger import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.
    raises:
        ValueError: If the yaml file is empty.
        BoxValueError: If the yaml file is malformed.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("yaml file is malformed")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they don't exist.

    Args:
        path_to_directories (list): List of paths to directories.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")




@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to save.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.
    Returns:
        ConfigBox: Loaded JSON data as a ConfigBox object.
    """
    with open(path, "r") as f:
        content = json.load(f)
        logger.info(f"JSON file loaded from: {path}")
        return ConfigBox(content)
    

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in a human-readable format.

    Args:
        path (Path): Path to the file.
    Returns:
        str: Size of the file in a human-readable format.
    """
    size_in_bytes = os.path.getsize(path)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    if size_in_mb >= 1:
        return f"{size_in_mb:.2f} MB"
    elif size_in_kb >= 1:
        return f"{size_in_kb:.2f} KB"
    else:
        return f"{size_in_bytes} Bytes"
    


def decode_base64_to_image(base64_string: str, output_path: Path):
    """
    Decodes a base64 string and saves it as an image file.

    Args:
        base64_string (str): Base64 encoded string of the image.
        output_path (Path): Path to save the decoded image file.
    """
    image_data = base64.b64decode(base64_string)
    with open(output_path, "wb") as f:
        f.write(image_data)
        logger.info(f"Image decoded from base64 and saved at: {output_path}")   
        f.close()

@ensure_annotations
def encode_image_to_base64(image_path: Path) -> str:
    """
    Encodes an image to a base64 string.

    Args:
        image_path (Path): Path to the image file.
    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        logger.info(f"Image at {image_path} encoded to base64 successfully.")
        return encoded_string
    