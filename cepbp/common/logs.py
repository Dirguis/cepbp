import logging
import configparser


class Logs(object):
    """
    Wrapper around the logging package.
    Amongst other things, allows to set up a path, a level and a name fpr the logger.
    The logger is a singleton and any handler added will be added on top of already exsiting handlers if a logger with the name already exists. This class handles that senario
      and makes sure that the logger is initialized only once. Otherwise, the same message could be duplicated.
    Finally, the class allows to print on the terminal and log in a text file at the same time.
    """
    def __init__(self):
        pass

    def get_logger(self, config=configparser.ConfigParser(), path='/tmp/', level='DEBUG', name='logger'):
        """
        Generates a logger, reusing an existing one if a logger with the same name is found, avoid the initialization step.
        The logger is stored at the class level, to allow other functions to act on it.

        Parameters
        ----------
        config: configparser object
          The logging information can come from a configuration file
        path: string
          local path where to store the logging file. Note, this is a path to a folder, not a file. The is named: name + '.txt'
        level: string
          More info on logging: https://docs.python.org/2/library/logging.html
        name: string
          name of the logger
        """
        if config.has_option('logs', 'path'):
            path = config['logs']['path']
        if config.has_option('logs', 'level'):
            level = config['logs']['level']

        self.logger = logging.getLogger(name)
        if len(self.logger.handlers) == 0:
            path = path + name + '.txt'
            level = getattr(logging, level)
            logFormatter = logging.Formatter("[%(levelname)-5.5s] [%(asctime)s] %(message)s",
                                             datefmt='%Y-%m-%d %H:%M:%S')
            fileHandler = logging.FileHandler(path)
            fileHandler.setFormatter(logFormatter)

            self.logger.addHandler(fileHandler)
            self.logger.setLevel(level)
        return

    def print_and_log(self, msg, msg_level='info'):
        """
        print message on the terminal and in a file

        Parameters
        ----------
        msg: string
          message to log
        msg_type: string
          level associated with the message. More info: https://docs.python.org/2/library/logging.html
        """
        print(msg)
        getattr(self.logger, msg_level)(msg)
        return
