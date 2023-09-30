#The argparse module makes it easy to write user-friendly command-line interfaces. The argparse module also automatically generates help and usage messages.
#The module will also issue errors when users give the program invalid arguments.
import argparse

#write messages about events happening in your code.
from loguru import logger

#if you write from terminal python wordstats.py --help you get the help documentation that you have written here
parser=argparse.ArgumentParser(prog='wordcount',description='Count the letter frequency in a text')
parser.add_argument('in file') #compulsory input
parser.add_argument('--plot', action='store_true',  #it's an optional argument that plot, store_true means that it's by default always off unless you specify otherwise
                    help='Plot a bar chat of the character frequencies ')

def process_file(file_path):
    #This is a doc string. It gives away the documentation of the function.
    """Process one file and count the occurrences of each characters.

    Arguments
    ---------
    file_path: string
        Path to the input file
    """
    #logger.info(f'Opening input file {file path}...'') #this is the correct string formation when you need to print also a variable
    with open(file_path) as input_file:
        data=input_file.read()
    logger.info(f'Done, {len(data)},character(s)found.')
    #.... do all the stuff
    if plot:
        logger.info('Plotting stuff...')

#Python module: you may want to execute from terminal or to import the module from terminal
#the following lines execute whatever you want from the module when called from terminal shell
#any statement that gets executed must be in a the definition of the function

if __name__=='__main__':
    args=parser.parse_args() #it's more like a dictionary that maps the arguments name with a key
    process_file(args.infile, args.plot)
