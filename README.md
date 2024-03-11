
# Dictionary Scraper

Simple little scraper of a well known dictionary site.

## Why

- I wanted to try using AWS Lambda
- I used similar scraping methods in a previous role. This was my attempt at writing something similar for myself.


## Results

- Lambda fail.
    - Lambda wants you to upload your dependencies and run them. lxml does some system specific compling on install which caused problems.
    - I started up an EC2 isntance using the same Amazon Linux distro that Lambda uses. Then I compiled my dependencies there and used a Layer to insert them into my Lambda pipeline. It seemed like a good idea, but it didn't work.
- I still like xpath for scraping.
    - Not a perfect parser. Plural words for example. But the main goal was just to write something to run on Lambda, which it did to... a point.

## Use

Just add the word you'd like to lookup to the end of the url.
Not a whole lot of actual practical use for this, but it was fun to make.

https://simple-dictionary.fly.dev/word

- [/mouse](https://simple-dictionary.fly.dev/mouse)

- [/house](https://simple-dictionary.fly.dev/house)

- [/carton](https://simple-dictionary.fly.dev/carton)
