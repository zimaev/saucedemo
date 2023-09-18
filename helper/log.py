import logging


def setup_logger():
    # Создание объекта логгера
    logger = logging.getLogger()

    # Установка уровня логирования (в данном случае INFO)
    logger.setLevel(logging.INFO)

    # Создание обработчика логов для вывода в консоль
    console_handler = logging.StreamHandler()

    # Установка формата вывода информации о логе
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)

    # Добавление обработчика логов к логгеру
    logger.addHandler(console_handler)

    return logger


# Использование функции для настройки логгера
logger = setup_logger()


