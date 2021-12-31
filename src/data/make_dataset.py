# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd
from loguru import logger
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """ 
    Convert input file to output file. 
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    dataset = pd.read_csv(input_filepath)
    dataset["experience"].fillna(0, inplace=True)
    dataset["test_score"].fillna(dataset["test_score"].mean(), inplace=True)

    dataset["experience"] = dataset["experience"].apply(lambda x: convert_to_int(x))
    logger.info("processing completed, generating the csv file for processed file")
    dataset.to_csv(output_filepath)


# Converting words to integer values
def convert_to_int(word):
    """
    Convert word to integer value. If word is not in the dictionary, return 0.  If word is in the dictionary, return the integer value. 
    """
    word_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "zero": 0,
        0: 0,
    }
    return word_dict[word]


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
