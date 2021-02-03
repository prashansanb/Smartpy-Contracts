import smartpy as sp

class TokenSwapper(sp.Contract):
    def __init__(self):
        self.init(counter = 0)
        
    @sp.entry_point
    def swap(self, params):
        lay = sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat).layout(("from_ as from", ("to_ as to", "value")))
        c = sp.contract(lay, params.tokenXContract, entry_point="transfer").open_some()
        data = sp.record(from_ = params.user_addr, to_ = params.admin_addr, value = params.value)
        sp.transfer(data, sp.mutez(0), c)
        lay2 = sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat).layout(("from_ as from", ("to_ as to", "value")))
        c = sp.contract(lay, params.tokenYContract, entry_point="transfer").open_some()
        data = sp.record(from_ = params.admin_addr, to_ = params.user_addr, value = params.value)
        sp.transfer(data, sp.mutez(0), c)

        
if "templates" not in __name__:
    @sp.add_test(name = "Tokens")
    def test():

        scenario = sp.test_scenario()
        scenario.h1("tokens test")

        scenario.table_of_contents()

        # sp.test_account generates ED25519 key-pairs deterministically:
        admin = sp.address("tz1a21nx5BggGmn4qr8QBPtZzKw6fs36isJY")
        alice = sp.test_account("Alice")
        bob   = sp.test_account("Robert")

        # Let's display the accounts:
        scenario.h1("Accounts")
        scenario.show([alice, bob])

        scenario.h1("Contract")
        c3 = TokenSwapper()
        scenario += c3
        scenario += c3.swap(value = 5, admin_addr = admin, user_addr = alice.address, tokenXContract=sp.address("KT1-AAA"), tokenYContract = sp.address("KT1-AAAAA"))
        
