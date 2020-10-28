#!/usr/bin/env python3
# -*- encoding: utf-8

from check_http_200 import check_http_200

def test_check_http_200_success():
    result = check_http_200("https://httpstat.us/200")

    assert result == {
        'failed': False,
        'status': 200,
        'url': 'https://httpstat.us/200'
    }


def test_check_http_200_failed():
    result = check_http_200("https://httpstat.us/500")

    assert result == {
        'failed': True,
        'status': 500,
        'url': 'https://httpstat.us/500'
    }
