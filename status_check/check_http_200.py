#!/usr/bin/env python3
# -*- encoding: utf-8

import sys

import click
import requests
from tabulate import tabulate

URLS_TO_CHECK = [
    'https://www-stage.wellcomecollection.org/works',
    'https://www-stage.wellcomecollection.org',
    'https://api-stage.wellcomecollection.org/catalogue/v2/works',
    'https://api-stage.wellcomecollection.org/catalogue/v2/images'
]


def check_http_200(url):
    try:
        response = requests.get(url)
        status = response.status_code
        response.raise_for_status()

        return {
            'url': url,
            'status': status,
            'failed': False
        }
    except requests.exceptions.HTTPError:
        return {
            'url': url,
            'status': status,
            'failed': True
        }


def _build_table(check_results):
    return [[result['url'], result['status']] for result in check_results]


if __name__ == "__main__":
    check_results = [check_http_200(url) for url in URLS_TO_CHECK]

    succeeded = _build_table([result for result in check_results if not result['failed']])
    failed = _build_table([result for result in check_results if result['failed']])

    click.echo(click.style(tabulate(succeeded), fg="green"))

    if failed:
        click.echo('')
        click.echo(click.style("Found failing checks!", fg="bright_red", underline=True))
        click.echo(click.style(tabulate(failed), fg="red"))
        sys.exit(1)
    else:
        click.echo(click.style("All checks passed", fg="bright_green", underline=True))
        click.echo('')





