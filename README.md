
# Dictionary Scraper

Simple little scraper of a well known dictionary site.

## Why

- I wanted to try using AWS Lambda
- I used similar scraping methods in a previous role. This was my attempt at writing something similar for myself.


## Results

- Lambda fail.
    - Lambda wants you to upload your dependencies and run them. lxml needs does some system specific setup on install which caused problems.
    - I tried using an EC2 instance of Amazon's Linux distro to compile the dependencies and add them directly into a Layer that way but it didn't work.
    - Ultimately ended up just sending it over to fly.dev
- I still like xpath for scraping.
    - Not a perfect parser. Plural words for example.

## Use

Just add the word you'd like to lookup to the end of the url.
Not a whole lot of actual practical use for this, but it was fun to make.

https://simple-dictionary.fly.dev/word

- [/mouse](https://simple-dictionary.fly.dev/mouse)

- [/house](https://simple-dictionary.fly.dev/house)

- [/carton](https://simple-dictionary.fly.dev/carton)
