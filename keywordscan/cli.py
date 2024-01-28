#!/usr/bin/env python

import argparse


def find_keywords(file_path, keyword_list, ignore=None):
    for name in ignore:
        if name in file_path:
            return

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            for keyword in keyword_list:
                if keyword.lower() in line.lower():
                    print(f"Keyword '{keyword}' found in {file_path} at line {line_number}: {line.strip()}")


def parse_args(argv):
    def parse_set(value):
        return set(value.split(","))

    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+")
    parser.add_argument(
        "--ignore", type=parse_set, default=set(), help="Ignore any files that contain one of these words in the path."
    )
    parser.add_argument(
        "-k", "--keywords", type=parse_set, default="eval", help="Scan these keywords."
    )

    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    print(args.filenames)
    print(args.keywords)
    print(args.ignore)
    for filename in args.filenames:
        find_keywords(filename, args.keywords, ignore=args.ignore)
    return


if __name__ == "__main__":
    sys.exit(main())
