import smartpy as sp


# A class of contracts
class MyExchanger(sp.Contract):
    def __init__(self):
        self.init(tokentypes = {
            "token1" : sp.int(100),
            "token2" : sp.int(100)
        })
        
    @sp.entry_point
    def swaptokens(self, value, token):
        #swapping only token1
        #sp.verify(self.data.tokentypes["token1"] >= value)
        self.data.tokentypes["token1"] -= value
        self.data.tokentypes["token2"] += value

# Tests
@sp.add_test(name = "Welcome")
def test():
    
    scenario = sp.test_scenario()
    scenario.h1("Welcome")
    c1 = MyExchanger()
    scenario += c1
    scenario += c1.swaptokens(value = sp.int(10), token = "token1")
    scenario += c1.swaptokens(value = sp.int(15), token = "token1")
    
    scenario.verify(c1.data.tokentypes["token1"] == 75)

