import hello

def test_hello(capfd):
    assert hello.hello("JEJE") is None
    out, err = capfd.readouterr()
    assert err == "Hello JEJE!"

def test_hello_world(capfd):
    assert hello.hello_world() is None
    out, err = capfd.readouterr()
    assert out == "Hello world!"
