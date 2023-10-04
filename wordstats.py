import argparse
import time 

from loguru import logger
import numpy as np
from unidecode import unidecode
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser(prog='wordcount',description='Count the letter frequency in a text')
parser.add_argument('in_file') 
parser.add_argument('--plot', action='store_true',  
                    help='Plot a bar chart of the character frequencies ')

def letterFrequency(file_path,plot):
    #This is a doc string. It gives away the documentation of the function.
    """Process one file and count the occurrences of each characters.

    Arguments
    ---------
    file_path: string
        Path to the input file
    --plot: boolean
    	If true, it will plot a hystogram of the occurences
    """
    logger.info(f'Opening input file {file_path}...')
    with open(file_path) as input_file:
        data=input_file.read()
        data=unidecode(data) #it clears the file from any characters that Python doesn't support
        
    start_time=time.time()
    alpha_char= list(filter(str.isalpha, data.lower())) #creates a list of all alphabetical characters (CASE INSENSITIVE)
    unique, counts = np.unique(np.array(alpha_char), return_counts=True) #returns unique values occured and their frequencies
    all_freq = dict(zip(unique, counts/len(alpha_char)))
    logger.info('Printing the relative frequence of each letter of the alphabet')
    print(all_freq)
    
    if plot:
        logger.info('Starting the histogram...')
        plt.bar(unique, counts)
        plt.title('Letter frequency')
        plt.xlabel('Letters')
        plt.ylabel('Occurences')
        plt.show()
        
    elapsed_time=time.time()-start_time
    print(f'Total elapsed time: {elapsed_time} seconds')
    logger.info('Done')

if __name__=='__main__':
    args=parser.parse_args() 
    letterFrequency(args.in_file, args.plot)
