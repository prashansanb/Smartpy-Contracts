
import smartpy as sp

def call(c, x):
    sp.transfer(x, sp.mutez(0), c)

class Token_X(sp.Contract):
#add contents of token_X smart contract
    @sp.entry_point
    

class Token_Y(sp.Contract):
    @sp.entry_point
#add contents of token_Y

class TokenSwapper(sp.Contract):
    def __init__(self, Token_X, Token_Y):
        self.init(Token_X  = Token_X,
                  Token_Y   = Token_Y,
                  counter = 0)
#value is x
    @sp.entry_point
    def swap_token(self, x):
        tk = sp.TRecord(k = sp.TContract(sp.TNat), x = sp.TNat)
        params = sp.record(k = sp.self_entry_point("burn"), x = x)
        call(sp.contract(tk, self.data.Token_X).open_some(), params)
        
        next_param = sp.record(k = sp.self_entry_point("mint"), x = x) 
        call(sp.contract(tk, self.data.Token_Y).open_some(), next_param)
        
        

    @sp.entry_point
    def reset(self, params):
        self.data.counter = 0



@sp.add_test(name = "Swapper")
def test():
    scenario = sp.test_scenario()
    
    token_x = Token_X()
    scenario += token_x
    token_y = Token_Y()
    scenario += token_y
    swapper = TokenSwapper(Token_X = token_x.address,
                      Token_Y  = token_y.address)
    scenario += swapper
    

