from unittest.mock import Mock

from connection import ConnectionHandler


def test_connect():
    external_obj = Mock()
    ConnectionHandler(external_obj)
    external_obj.connect.assert_called_with()
