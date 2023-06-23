"""Module to generate random users"""
from faker import Faker
import logging
from pathlib import Path

from typing import List

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log', level=logging.WARNING)

fake = Faker(locale="fr_FR")


def get_user() -> str:
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user...")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(nb_users: int) -> List[str]:
    """Generate a list of users

    Args:
        nb_users (int): Number of user to generate

    Returns:
        list[str]: users
    """
    logging.info(f"Generating a list of {nb_users} users...")
    return [get_user() for _ in range(nb_users)]


if __name__ == "__main__":
    user = get_users(3)
    print(user)
