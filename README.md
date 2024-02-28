
# Dictionary Scraper

Simple little scraper of a well known dictionary site.

## Why

- I wanted to try using AWS Lambda
- I used similar scraping methods but never made note of how the code worked. This was my attempt at doing something similar for myself.


## Results

- Lambda fail.
    - Lambda wants you to upload your dependencies and run them. lxml needs does some system specific setup on install.
    - I tried using an EC2 instance of Amazon's Linux distro, but I couldn't get it to work.
    - Ultimately ended up just sending it over to fly.io.
- I still like xpath for scraping.
    - Not a perfect scraper. There are some html formats that I haven't handled. Plural words

## Use

https://simple-dictionary.fly.dev/<word>

[mouse](https://simple-dictionary.fly.dev/mouse)

[house](https://simple-dictionary.fly.dev/house)

[carton](https://simple-dictionary.fly.dev/carton)