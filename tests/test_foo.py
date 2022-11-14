from foo import foo


def test_foo():
    assert foo() == "foo"


def test_foo_upper():
    assert foo(True) == "FOO"
