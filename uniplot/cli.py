import argparse
from . import parse
from . import analysis

LOC="uniprot_receptor.xml.gz"

def average(args):
    print("Average length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))
    ))

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    handle = gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record.name)


def cli():
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)

    args = parser.parse_args()

    args.func(args)

