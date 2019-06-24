#!/usr/bin/env python

import sys
import re
import argparse

from text import text_to_sequence, sequence_to_text

# From keithito/tacotron.
# Comma-separated list of cleaners to run on text prior to training and eval. For non-English
# text, you may want to use "basic_cleaners" or "transliteration_cleaners".
cleaners='english_cleaners'

def postprocess(text):

    # Replace '-' with space
    text = text.replace('-', ' ')

    # Remove '~'(end of sequence)
    text = re.sub('~', '', text)

    # Replace '.' with space
    text = text.replace('.', ' ')

    # Replace ',' with space
    text = text.replace(',', ' ')

    # Strip white spaces in the beginning and the end of text.
    text = text.strip()

    # append line end
    text += '\n'

    # uppercase
    text = text.upper()

    return text

def main():

    parser = argparse.ArgumentParser(description='English text to sequence.')
    parser.add_argument('input', help='Input text file')
    parser.add_argument('output', help='Output .lab file')
    parser.add_argument('--raw', dest='raw', action='store_true',
                    help='Output raw sequence(contain some non-alphabet characters. not an .lab compatible text)')

    args = parser.parse_args()

    f = open(args.input, 'r')
    text = f.read()

    cleaner_names = [x.strip() for x in cleaners.split(',')]
    seq = text_to_sequence(text, cleaner_names)

    lab_text = sequence_to_text(seq)
    if not args.raw:
        # Remove non-alphabet character
        lab_text = postprocess(lab_text)

    with open(args.output, 'w') as of:
        of.write(lab_text)

if __name__ == '__main__':
    main()
