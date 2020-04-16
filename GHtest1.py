# example of a class setup and initialisation
class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test_function(self):
        return self.x*2

tc = TestClass(4,3)

print(tc.test_function())
