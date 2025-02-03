from helloworld.app import greeting

def test_name():
    """
    If a name is provided, the greeting includes the name
    """
    
    assert greeting("Alice") == "Hello, Alice"
    
def test_empty():
    """
    If a name is not provided, a generic greeting is provided
    """
    
    assert greeting("") == "Hello, stranger"
    
def test_brutus():
    """
    If the name is Brutus, a special greeting is provided
    """
    
    assert greeting("Brutus") == "BeeWare the IDEs of Python!"