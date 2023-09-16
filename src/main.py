import pathlib
import argparse
from VocTutor import VocTutor


def parse_arg():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument_group('Optional arguments')
    optional.add_argument("-r", "--root_dir", dest="root_dir", required=False, default='D:\\pyVocTutor',
                          help="Root directory to put config file and data file.",
                          type=lambda s: pathlib.Path(s).absolute(), )
    return parser.parse_args()


def main():
    args = parse_arg()
    # create VocTutorWindow object
    vocTutor = VocTutor(args.root_dir)
    vocTutor.run()


if __name__ == '__main__':
    main()
