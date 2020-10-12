from unittest.mock import patch

from .fileinfo import FileInfo


def test_init():
    file_name = 'somefile.ext'
    fi = FileInfo(file_name)
    assert fi.file_name == file_name


def test_init_relative():
    file_name = 'somefile.ext'
    relative_path = '../{}'.format(file_name)
    fi = FileInfo(relative_path)
    assert fi.file_name == file_name


@patch('os.path.getsize')
@patch("os.path.abspath")
def test_get_info(mock_path, mock_size):
    file_name = 'somefile.ext'
    original_path = '../{}'.format(file_name)

    test_path = "test/path"
    mock_path.return_value = test_path

    test_size = 1234
    mock_size.return_value = test_size

    fi = FileInfo(original_path)
    info = fi.get_info()

    mock_path.assert_called_with(file_name)
    mock_size.assert_called_with(file_name)
    assert info == (file_name, original_path, test_path, test_size)
