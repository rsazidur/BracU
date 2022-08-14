class SultansDine:
    branches = 0
    total_sell = 0
    branch_list = []

    def __init__(self, name, branch_sell=0):
        self.name = name
        self.sell = branch_sell
        SultansDine.branch_list.append(self.name)
        SultansDine.branches += 1

    def sellQuantity(self, quantity):
        if quantity < 10:
            branch_sell = int(quantity) * 300
        elif quantity < 20:  
            branch_sell = int(quantity) * 350
        else:
            branch_sell = int(quantity) * 400
        
        self.branch_sell = branch_sell
        SultansDine.total_sell += branch_sell
        SultansDine.branch_list[len(SultansDine.branch_list)-1].append(self.branch_sell)

    def branchInformation(self):
        print(f'Branch Name: {self.name}\nBranch Sell: {self.branch_sell} Taka')

    @classmethod
    def branch_details(cls):
        for i in SultansDine.branch_list:
            print(f'Branch Name: {i[0]}\nBranch consists of total sell\'s: {(i[1]/SultansDine.total_sell) * 100}')
    
    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.branches}")
        print(f"Total Sell: {SultansDine.total_sell} Taka")
        SultansDine.branch_details()


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()