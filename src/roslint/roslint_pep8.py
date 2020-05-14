from . import pycodestyle

def main():
    pycodestyle.MAX_LINE_LENGTH = 120
    pycodestyle._main()

if __name__ == '__main__':
    main()
