#!/usr/bin/env python3
# -*- encoding: utf-8

from rank_eval import rank_eval


def test_rank_eval():
    result = rank_eval()
    assert ('failed' in result) == True
