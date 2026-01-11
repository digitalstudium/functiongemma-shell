import os

from transformers.utils import get_json_schema

# --- PATHS CONFIGURATION ---
DATA_DIR = "prepared_data"
PATH_TRAIN = os.path.join(DATA_DIR, "train")
PATH_TEST = os.path.join(DATA_DIR, "test")

DEFAULT_SYSTEM_MSG = (
    "You are a model that can do function calling with the following functions"
)


# --- TOOLS DEFINITIONS ---
# Реализация не нужна, нужны только docstrings и типы для схемы
def check_website(url: str) -> str:
    """
    Check website availability (HTTP status).
    Args:
        url: Website address (e.g., "google.com" or "https://github.com").
    Returns:
        JSON string containing status code.
    """
    pass


def find_largest_file(directory: str = ".") -> str:
    """
    Find the largest file in a directory using bash commands.
    Args:
        directory: Directory path to search in. Defaults to current directory.
    Returns:
        JSON string with information about the largest file found.
    """
    pass


def get_system_info() -> str:
    """
    Get basic system information: OS, kernel, memory, disk.
    Returns:
        JSON string with system information
    """
    pass


# Генерация схем
TOOLS = [
    get_json_schema(find_largest_file),
    get_json_schema(get_system_info),
    get_json_schema(check_website),
]
