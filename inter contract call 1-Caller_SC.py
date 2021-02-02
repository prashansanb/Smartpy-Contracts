#note-> here it is only possible to verify calls if we deploy on test nodes 

import smartpy as sp
class CallerContract(sp.Contract):
    def __init__(self):
        self.init(mynum = sp.int(0))
        
    @sp.entry_point
    def sendDataToTargetContract(self,params):
        c = sp.contract(sp.TRecord(num = sp.TInt),params.targetContract,entry_point="addTwoAndReturn").open_some()
        mydata = sp.record(num = params.num)
        sp.transfer(mydata,sp.mutez(0),c)
        
        
    @sp.entry_point
    def recieveResponse(self,params):
        self.data.mynum = params.ans
        
        
@sp.add_test(name="Inter contract calling test")
def test():
    obj = CallerContract()
    scenario = sp.test_scenario()
    scenario += obj
    #scenario+=obj.sendDataToTargetContract(num=2,targetContract=sp.address("KT1-AAA")).run(amount=sp.mutez(0))
    #scenario+=obj.recieveResponse(ans=4)
