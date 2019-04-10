import hello

def test_hello(capfd):
    assert hello.hello("JEJE") is None
    out = capfd.readouterr().out
    assert out == "Hello, JEJE!\n"

def test_hello_world(capfd):
    assert hello.hello_world() is None
    out = capfd.readouterr().out
    assert out == "Hello, world!\n"
