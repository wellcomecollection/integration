#!/usr/bin/env python3
# -*- encoding: utf-8

import argparse
import os
import sys
from urllib.request import urlopen


def check_http_200(url):
    with urlopen(url) as response:
        status = response.status
        if status is not 200:
            raise Exception(f"url: {url} returned status {status}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    url = args.url

    try:
        print(f"Checking for 200 @ {url}")
        check_http_200(url)
        print(f"Passed: 200 @ {url} found")
        sys.exit(0)
    except Exception as err:
        print(f"Failed: {err} @ {url} found")
        sys.exit(1)
