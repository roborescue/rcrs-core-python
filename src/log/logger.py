import logging
import logging.handlers


class Logger:
    def __init__(self, _name, agent_id=0) -> None:

        self.root = logging.getLogger(_name)
        if not self.root.hasHandlers():
            self.file_handler = logging.handlers.RotatingFileHandler(filename='logs/' + _name + '.log', mode='a')
            self.console_handler = logging.StreamHandler()
            # formatter = logging.Formatter(f'%(processName)-10s %(levelname)-3s %(name)s ({agent_id}): %(message)s')
            formatter = logging.Formatter(f'%(levelname)-3s %(name)s({agent_id}): %(message)s')
            self.file_handler.setFormatter(formatter)
            self.console_handler.setFormatter(formatter)
            self.root.addHandler(self.file_handler)
            self.root.addHandler(self.console_handler)
            self.root.setLevel(logging.DEBUG)
            # self.root.propagate = False

    def info(self, msg):
        self.root.info(msg)

    def debug(self, msg):
        self.root.debug(msg)

    def error(self, msg):
        self.root.error(msg)

    def warning(self, msg):
        self.root.warning(msg)

    def warn(self, msg):
        self.root.warn(msg)

    def set_id(self, id):
        try:
            self.root.removeHandler(self.file_handler)
            self.root.removeHandler(self.console_handler)

            formatter = logging.Formatter(f'%(levelname)-3s %(name)s({id}): %(message)s')
            self.file_handler.setFormatter(formatter)
            self.console_handler.setFormatter(formatter)
            self.root.addHandler(self.file_handler)
            self.root.addHandler(self.console_handler)

        except Exception as ex:
            print(ex)


