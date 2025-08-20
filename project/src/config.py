from dotenv import load_dotenv
from typing import Optional
import os

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)


if __name__ == '__main__':
    pass