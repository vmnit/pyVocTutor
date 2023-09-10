# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from VocTutor import VocTutor

ROOT_DIR = 'D:\pyVocTutor'

def main():
    # create VocTutorWindow object
    vocTutor = VocTutor(ROOT_DIR)
    vocTutor.run()


if __name__ == '__main__':
    main()
