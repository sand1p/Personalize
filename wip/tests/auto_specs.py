from unittest import TestCase, mock


class Target(object):
    def apply(value, are_you_sure):
        if are_you_sure:
            return value
        else:
            return None


def method(target, value):
    return target.apply(value)


class MethodTestCase(TestCase):

    def test_method(self):
        target = mock.Mock()
        method(target, "value")

        target.apply.assert_called_with("value")


