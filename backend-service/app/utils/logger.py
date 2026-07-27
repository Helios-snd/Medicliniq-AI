import logging


class Logger:
    _instance = None

    @staticmethod
    def get_logger(level:int = logging.INFO) -> logging.Logger:


        """

        Returns a only one logger instance
        Ensures that call to get_logger() returns the same logger object

        """

        if Logger._instance is not None:
            return Logger._instance
        
        logger = logging.getLogger("app")
        logger.setLevel(level)
        logger.propagate = False

        if not logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        Logger._instance = logger
        return logger

logger = Logger.get_logger()

