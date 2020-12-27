import logging

logging.basicConfig(filename='test.log',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(funcName)s')


def func():
    logging.info('info message')


if __name__ == '__main__':
    func()
