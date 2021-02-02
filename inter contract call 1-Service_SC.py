#needs to be  deployed on test net first, calls back the initial contract that had called it

import smartpy as sp
class TargetContract(sp.Contract):
        
    @sp.entry_point
    def addTwoAndReturn(self,params):
        contractParams = sp.contract(sp.TRecord(ans = sp.TInt),sp.sender,entry_point="recieveResponse").open_some()
        
        dataToBeSent = sp.record(ans = params.num+2)
        sp.transfer(dataToBeSent,sp.mutez(0),contractParams)
        
    @sp.entry_point
    def addThreeAndReturn(self,params):
        contractParams = sp.contract(sp.TRecord(ans = sp.TInt),sp.sender,entry_point="recieveResponse").open_some()
        
        dataToBeSent = sp.record(ans = params.num+3)
        sp.transfer(dataToBeSent,sp.mutez(0),contractParams)
        
@sp.add_test(name="Inter contract calling test")
def test():
    obj = TargetContract()
    scenario = sp.test_scenario()
    scenario+=obj
    #scenario+=obj.addTwoAndReturn(num=4).run(sender=sp.address("KT1-AAA"),amount=sp.mutez(0))
