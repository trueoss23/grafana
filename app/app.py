from loguru import logger
import time

logger.add("/var/log/app.log", rotation="10 MB", level="INFO")


def app():
    for _ in range(100):
        logger.info("Это информационное сообщение")
        logger.warning("Это предупреждающее сообщение")
        logger.error("Это сообщение об ошибке")
        time.sleep(10)


if __name__ == "__main__":
    app()

