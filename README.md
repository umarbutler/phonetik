# phonetik
## About
[Hermitdave's FrequencyWords list](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/ar/ar_50k.txt) of the 50,000 most frequent Arabic words, was used to query [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Main_Page). Arabic words (with diacritical marks) and their transliterations/romanizations (in the Latin script) were extracted from the queried Wiktionary pages (the code used to scrape Wiktionary is available [here](https://github.com/umarbutler/phonetik/blob/main/scraper/main.py)). The resulting data is available, in .csv format (comma delimited), [here](https://github.com/umarbutler/phonetik/blob/main/dataset/raw/output.csv).

A [script](https://github.com/umarbutler/phonetik/tree/main/scripts/preprocess.py) was used to remove duplicates and words begining, or ending, with a '-', from the scraped data (this script can be modified, if necessary, to include those words). The resulting processed data is available [here](https://github.com/umarbutler/phonetik/blob/main/dataset/processed).

## License
[Hermitdave's FrequencyWords list](https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/ar/ar_50k.txt) is licensed under CC-BY-SA-4.0. [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Main_Page) is licensed under CC BY-SA 3.0.

All unique code in this project is licensed under GNU GPLv3. The corpus, itself, is licensed under CC BY-SA 3.0.

## Citation

You may cite this corpus using the following citation:

> Butler, U. phonetik. 2020, https://github.com/umarbutler/phonetik/.
