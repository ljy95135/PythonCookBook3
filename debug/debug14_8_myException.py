class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

"""
>>> try:
... raise RuntimeError('It failed')
... except RuntimeError as e:
... print(e.args)
...
('It failed',)
>>> try:
... raise RuntimeError('It failed', 42, 'spam')
... except RuntimeError as e:
... print(e.args)
...
('It failed', 42, 'spam')
>>>
"""