# English text to sequence

English text to sequcen converts input English text into a text which contains only alphabets.
This converter is primarily for creating `.lab` file. `.lab` is used for the alignment of speech audio(e.g. Montreal Forced Aligner https://montreal-forced-aligner.readthedocs.io/en/latest/)

For example, "The answer is 42." are converted to "THE ANSWER IS FORTY TWO".

## Requirements

* Python 3.2+

## License

MIT license.

## How to use

Assume input is ASCII text.

```
$ python english-text-to-sequence.py input.txt output.lab
```


### Third party license.


* inflect. Copyright Jason R. Coombs. MIT license
* text/ scripts.  Copyright (c) 2017 Keith Ito. MIT license.
