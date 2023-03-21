import asyncio
import json

from telminal import PACKAGE_PATH
from telminal import Telminal


async def amain():
    try:
        with open(PACKAGE_PATH / "config.json", encoding="utf-8") as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {
            "api_id": 17983098,
            "api_hash": "ee28199396e0925f1f44d945ac174f64",
            "token": "5714654934:AAFm0UBvzuU1X-Adg7QThWCzpoKBww9SNXE",
        }

    telminal = Telminal(**config)
    await telminal.start()


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
