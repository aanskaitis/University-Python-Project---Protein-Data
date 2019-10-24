import argparse
from . import parse
from . import plot
from . import analysis

LOC="uniprot_receptor.xml.gz"

def average(args):
    """This function prints the average length length of lists in set"""
    print("Average length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))
    ))

def dump(args):
    """This function prints out all the records"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    """This function prints out all names of the records"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def plot_average_by_taxa(args):
    """This function shows the bar chart of the average length of different proteins by taxa"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC), input("Choose depth = "))
    plot.plot_bar_show(av)

def plot_pie_average_by_taxa(args):
    """This function shows the pie chart of the average length of different proteins by taxa"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC),input("Choose depth = "))
    plot.plot_pie_show(av)


def cli():
    """This function creates a new parser, adds all the subparsers and calls the function"""
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="You can use 4 functions:")

    ## Add subparsers
    subparsers.add_parser("dump",help="To print out all the records").set_defaults(func=dump)
    subparsers.add_parser("list",help="To print out the names of protein sequences").set_defaults(func=names)
    subparsers.add_parser("average",help= "To print out an average length of one protein sequence").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa",help="To show the bar chart of average length of proteins sequences by taxa. "
                                                      "You have to choose the depth of taxa, write 1 for default and 2 for more detailed.")\
        .set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("plot-pie-average-by-taxa",help="To show the pie chart of average length of proteins sequences by taxa. "
                                                          "You have to choose the depth of taxa, write 1 for default and 2 for more detailed.")\
        .set_defaults(func=plot_pie_average_by_taxa)

    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it.
    args.func(args)

