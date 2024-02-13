import os
from box.exceptions import BoxValueError
import yaml
import cnnClassifier
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any 
import base64

import os
import json
import yaml
import pickle
from typing import Dict, Any

def read_yaml(file_path: str) -> Dict[str, Any]:
    """
    Read data from a YAML file.

    Parameters:
    - file_path (str): The path to the YAML file.

    Returns:
    - data (dict): The data read from the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        print(f"Error reading YAML file '{file_path}': {e}")
        return {}

def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """
    Save data to a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.
    - data (dict): The data to be saved.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to JSON file: {file_path}")
    except Exception as e:
        print(f"Error saving data to JSON file '{file_path}': {e}")

def create_directory(directory_path: str) -> None:
    """
    Create a directory if it does not exist.

    Parameters:
    - directory_path (str): The path to the directory.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory created: {directory_path}")
    except Exception as e:
        print(f"Error creating directory '{directory_path}': {e}")

def load_json(file_path: str) -> Dict[str, Any]:
    """
    Load data from a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.

    Returns:
    - data (dict): The data loaded from the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error loading data from JSON file '{file_path}': {e}")
        return {}

def save_binary(file_path: str, data: Any) -> None:
    """
    Save binary data to a file using pickle.

    Parameters:
    - file_path (str): The path to the binary file.
    - data (any): The binary data to be saved.
    """
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
        print(f"Binary data saved to file: {file_path}")
    except Exception as e:
        print(f"Error saving binary data to file '{file_path}': {e}")
