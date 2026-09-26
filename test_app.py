from app import hello, farewell, shout, whisper


def test_hello(capsys):
    hello()
    assert capsys.readouterr().out == "Hello, world!\n"


def test_farewell(capsys):
    farewell()
    assert capsys.readouterr().out == "Goodbye for now!\n"


def test_shout(capsys):
    shout()
    assert capsys.readouterr().out == "WATCH OUT!\n"


def test_whisper(capsys):
    whisper()
    assert capsys.readouterr().out == "...quietly does the thing...\n"
