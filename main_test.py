# -*- coding: utf-8 -*-
import mock
import pytest


def test_init():
    from . import main

    with mock.patch.object(main, "main", return_value=42):
        with mock.patch.object(main, "__name__", "__main__"):
            with mock.patch.object(main.sys, "exit") as mock_exit:
                main.init()
                assert mock_exit.call_args[0][0] == 42
