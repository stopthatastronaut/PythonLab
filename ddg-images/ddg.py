import requests;
import re;
import json;
import time;
import logging;

logging.basicConfig(level=logging.DEBUG);
logger = logging.getLogger(__name__)

# this one adapted from https://github.com/deepanprabhu/duckduckgo-images-api

def search(keywords, max_results=None):
    url = 'https://duckduckgo.com/';
    params = {
    	'q': keywords
    };

    logger.debug("Hitting DuckDuckGo for Token");

    #   First make a request to above URL, and parse out the 'vqd'
    #   This is a special token, which should be used in the subsequent request
    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I);

    if not searchObj:
        logger.error("Token Parsing Failed !");
        return -1;

    logger.debug("Obtained Token");

    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('l', 'us-en'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '1'),
        ('v7exp', 'a'),
    )

    requestUrl = url + "i.js";

    logger.debug("Hitting Url : %s", requestUrl);

    y = 0

    while True:
        while True:
            try:
                res = requests.get(requestUrl, headers=headers, params=params);
                data = json.loads(res.text);
                break;
            except ValueError as e:
                logger.debug("Hitting Url Failure - Sleep and Retry: %s", requestUrl);
                time.sleep(5);
                continue;

        logger.debug("Hitting Url Success : %s", requestUrl);
        printJson(data["results"], y);

        if "next" not in data:
            logger.debug("No Next Page - Exiting");
            exit(0);

        requestUrl = url + data["next"];


def printJson(objs, y):
    x = 0
    y = y + 1
    for obj in objs:
        print(obj)
        print("Width {0}, Height {1}".format(obj["width"], obj["height"]))
        print("Thumbnail {0}".format(obj["thumbnail"]))
        print("Url {0}".format(obj["url"]))
        print("Title {0}".format(obj["title"].encode('utf-8')))
        print("Image {0}".format(obj["image"]))
        print("__________")
        x = x + 1
        print("{0}-{1}".format(y, x))
        saveImage(obj["image"], "{0}-{1}".format(y,x))

def saveImage(url, keyword):
    img_link = url
    img_data = requests.get(img_link).content

    filename = "imgout/" + keyword + ".png"
    with open(filename, 'wb+') as f:
        f.write(img_data)

    print("File " + keyword + ".png successfully downloaded.")


while True:
    keyword = input('Enter the search keyword : ')
    # print(keyword)
    search(keyword)