from unittest.mock import Mock

from .connection import ConnectionHandler


def test_connect():
    external_obj = Mock()
    ConnectionHandler(external_obj)
    external_obj.connect.assert_called_with()


def test_setup():
    external_obj = Mock()
    ch = ConnectionHandler(external_obj)
    ch.set_up()
    external_obj.set_up.assert_called_with(cache=True, max_connections=256)
