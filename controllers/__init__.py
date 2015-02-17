from Test import Test
from Top import Top

__all__ = ['Test', 'Top']

def getRouting():
    return [
        ('/Test', Test),
        ('/Top', Top)
    ]
