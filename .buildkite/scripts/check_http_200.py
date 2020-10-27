#!/usr/bin/env python3
# -*- encoding: utf-8

import argparse
import os
import requests
from requests.exceptions import HTTPError, RequestException
import sys


def check_http_200(url):
    resp = requests.get(url)
    resp.raise_for_status()


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
    except HTTPError as err:
        print(f"Failed: {err.response.status_code} @ {url} found")
        sys.exit(1)
    except RequestException as err:
        print(f"Failed: {err} @ {url} found")
        sys.exit(1)
