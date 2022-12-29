


import os
import logging
import logging.config

logging.config.fileConfig('config.ini')
consolelogger = logging.getLogger('ConsoleOutput')
filelogger = logging.getLogger()

def main():
	print('heworld')

if __name__ == '__main__':
	main()


