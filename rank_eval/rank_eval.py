#!/usr/bin/env python3
# -*- encoding: utf-8

import sys

import click
import requests
from tabulate import tabulate

RANK_EVAL_URL = 'https://rank.wellcomecollection.org/api/eval'
TEST_ENV = 'stage'


def rank_eval():
    try:
        response = requests.get(f'{RANK_EVAL_URL}?env={TEST_ENV}')
        response.raise_for_status()
        json = response.json()

        return {
            'failed': not json['success']
        }
    except requests.exceptions.HTTPError:
        return {
            'failed': True
        }


if __name__ == "__main__":
    failed = rank_eval()['failed']

    if failed:
        click.echo('')
        click.echo(click.style("Rank eval failed!",
                               fg="bright_red", underline=True))
        click.echo(click.style(tabulate(failed), fg="red"))
        sys.exit(1)
    else:
        click.echo(click.style("Rank eval passed",
                               fg="bright_green", underline=True))
        click.echo('')
