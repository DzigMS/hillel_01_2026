import logging



def config():
    console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.WARNING)

    # file_handler = logging.FileHandler('file_logger.log')

    logging.basicConfig(handlers=[console_handler],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.NOTSET)