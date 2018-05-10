# conventional rules
class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # A public attribute

    def public_method(self):
        """
        A public method
        """
        pass

    def _internal_method(self):
        pass


# can't inherit
class B:
    def __init__(self):
        self.__private = 0  # _B__private

    def __private_method(self):  # _B__private_method
        pass

    def public_method(self):
        pass
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        # _C__private
        self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):  # _C__private_method
        pass
