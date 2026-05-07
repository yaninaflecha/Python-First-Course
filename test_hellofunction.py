from hellofunction import hello

def test_default():
   
    hello()== "hello, world"

def test_argument():
    for name in ["Harry", "Ron","Hermione"]:
        assert hello(name)== f"hello, {name}"