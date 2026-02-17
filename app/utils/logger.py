import logging
import os
from app.config.settings import Settings

def setup_logger():
    os.makedirs(Settings.LOG_DIR, exist_ok=True)

    log_path = os.path.join(Settings.LOG_DIR, "app.log")

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()
