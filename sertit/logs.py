""" Logging tools """
import os
import logging
from datetime import datetime
from colorlog import ColoredFormatter

LOGGING_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
SU_NAME = 'sertit'


def init_logger(curr_logger: logging.Logger,
                log_lvl: int = logging.DEBUG,
                log_format: str = LOGGING_FORMAT) -> None:
    """
    Initialize a very basic logger to trace the first lines in the stream.

    To be done before everything (like parsing log_file etc...)

    ```python
    >>> logger = logging.getLogger("logger_test")
    >>> init_logger(logger, logging.INFO, '%(asctime)s - [%(levelname)s] - %(message)s')
    >>> logger.info("MESSAGE")
    2021-03-02 16:57:35 - [INFO] - MESSAGE
    ```

    Args:
        curr_logger (logging.Logger): Logger to be initialize
        log_lvl (int): Logging level to be set
        log_format (str): Logger format to be set
    """
    curr_logger.setLevel(log_lvl)
    formatter = logging.Formatter(log_format)

    # Set stream handler
    if curr_logger.handlers:
        curr_logger.handlers[0].setLevel(log_lvl)
        curr_logger.handlers[0].setFormatter(formatter)
    else:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_lvl)
        stream_handler.setFormatter(formatter)
        curr_logger.addHandler(stream_handler)


# pylint: disable=R0913
# Too many arguments (6/5) (too-many-arguments)
def create_logger(logger: logging.Logger,
                  file_log_level: int,
                  stream_log_level: int,
                  output_folder: str,
                  name: str,
                  other_logger_names: list = None) -> None:
    """
    Create file and stream logger with colored logs.

    ```python
    >>> logger = logging.getLogger("logger_test")
    >>> create_logger(logger, logging.DEBUG, logging.INFO, "path\\to\\log", "log.txt")
    >>> logger.info("MESSAGE")
    2021-03-02 16:57:35 - [INFO] - MESSAGE

    >>> # "logger_test" will also log DEBUG messages
    >>> # to the "path\\to\\log\\log.txt" file with the same format
    ```

    Args:
        logger (logging.Logger): Logger to create
        file_log_level (int): File log level
        stream_log_level (int): Stream log level
        output_folder (str): Output folder
        name (str): Name of the log
        other_logger_names (list): Other existing logger to manage (setting the right format and log level)
    """
    # Logger data
    date = datetime.today().replace(microsecond=0).strftime("%y%m%d_%H%M%S")
    log_file_name = f"{date}_{name}_log.txt"

    # Remove already created console handler
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)

    # Add stream handler
    color_fmt = ColoredFormatter(
        "%(asctime)s - [%(log_color)s%(levelname)s%(reset)s] - %(message_log_color)s%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'cyan',
            'ERROR': 'red',
            'CRITICAL': 'fg_bold_red,bg_white',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'white',
                'INFO': 'green',
                'WARNING': 'cyan',
                'ERROR': 'red',
                'CRITICAL': 'bold_red'
            }
        },
        style='%'
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_log_level)
    stream_handler.setFormatter(color_fmt)
    logger.addHandler(stream_handler)

    # Get logger file output path
    log_path = os.path.join(output_folder, log_file_name)

    # Create file handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(file_log_level)
    file_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    logger.addHandler(file_handler)

    # Manage other loggers
    if other_logger_names:
        for log_name in other_logger_names:
            other_logger = logging.getLogger(log_name)

            # Remove all handlers (brand new logger)
            other_logger.handlers = []

            # Set the right format and log level
            # Set log to info as these other loggers are not really important
            other_logger.setLevel(logging.INFO)
            other_logger.addHandler(stream_handler)
            other_logger.addHandler(file_handler)


def shutdown_logger(logger: logging.Logger) -> None:
    """
    Shutdown logger (if you need to delete the log file for example)

    ```python
    >>> logger = logging.getLogger("logger_test")
    >>> shutdown_logger(logger)
    >>> # "logger_test" won't log anything after another init
    ```

    Args:
        logger (logging.Logger): Logger to shutdown
    """
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.flush()
        handler.close()


def reset_logging() -> None:
    """
    Reset root logger

    **WARNING: MAY BE OVERKILL**

    ```python
    >>> reset_logging()
    Reset root logger
    ```

    """
    manager = logging.root.manager
    manager.disabled = logging.NOTSET
    for logger in manager.loggerDict.values():
        if isinstance(logger, logging.Logger):
            logger.setLevel(logging.NOTSET)
            logger.propagate = True
            logger.disabled = False
            logger.filters.clear()
            handlers = logger.handlers.copy()
            for handler in handlers:
                # Copied from `logging.shutdown`.
                try:
                    handler.acquire()
                    handler.flush()
                    handler.close()
                except (OSError, ValueError):
                    pass
                finally:
                    handler.release()
                logger.removeHandler(handler)
