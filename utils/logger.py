import logging
import os

def get_logger():
    os.makedirs("Logs",exist_ok=True)

    logging.basicConfig(
        filename="Logs/execution.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)m",
        level=logging.INFO
    )
    return logging.getLogger()