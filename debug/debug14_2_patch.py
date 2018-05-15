from unittest.mock import patch
import example


@patch('example.func')
def test1(x, mock_func):
    example.func(x)  # Uses patched example.func
    mock_func.assert_called_with(x)


with patch('example.func') as mock_func:
    example.func(x)  # Uses patched example.func
    mock_func.assert_called_with(x)

p = patch('example.func')
mock_func = p.start()
example.func(x)
mock_func.assert_called_with(x)
p.stop()

# @patch('example.urlopen', return_value=sample_data)
