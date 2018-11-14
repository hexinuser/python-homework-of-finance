

from a4task1 import *

def collect_bids(filename):
    """ process the data file containing the bids
        input filname: str
    """
    bids = []
    fr = open(filename,'r')
    for line in fr.readlines()[1:]:
        line = line.strip().split(',')
        line[0] = int( line[0])
        line[1] = int( line[1])
        line[2] = float(line[2])
        bids.append(line)
    return bids

bids = collect_bids('./bond_bids.csv')
    
def print_bids(bids):
    """ process the a of bids, and produce a beautifully-formatted table of the bids. 
        input bids: list    
    """
    print('Bid ID        Bid Amount         Price')
    for i in range(len(bids)):
        print('%3d        $%-10d       $  %-5.3f'%(bids[i][0],bids[i][1],bids[i][2]))

#print_bids(bids)  \
        
#r = bond_yield_to_maturity(100, 0.03, 5, 2, 99.5)
        
def find_winning_bids(bids, total_offering_fv, c, n, m):
    """ processes a list of bids and determine which are successful in the auction
        input bids:list; total_offering_fv, c: float; n, m: int
    """
    bids = sorted(bids,key= lambda x:(x[2],x[1]),reverse=True)
    
    print('Here are all of the bids, sorted by price descending: ')
    print_bids(bids)
    
    bid_amount = [x[1] for x in bids]
    
    for i in range(len(bid_amount)):
        if sum(bid_amount[:i+1])>=total_offering_fv:
            bids[i][1] = total_offering_fv-sum(bid_amount[:i])
            break
    for j in range(i+1,len(bid_amount)):
        bids[j][1] = 0 
        
    print('The auction is for $%.2f of bonds.' %total_offering_fv)
    print('%d bids were successful in the auction.'%(i+1))
    clear_price = bids[i][2]
    ytm = bond_yield_to_maturity(100, c,n,m, clear_price)
    print('The auction clearing price was $%.3f, i.e., YTM is %.6f per year.'%(clear_price,ytm))
    print('Here are the results for all bids:')
    print_bids(bids)
    return bids
    
#if __name__ == '__main__':
#
#    # read in the bids
#    bids = collect_bids('./bond_bids.csv')
#    print("Here are all the bids:")
#    print_bids(bids)
#    print()
#
#    processed_bids = find_winning_bids(bids, 1400000, 0.0325, 5, 2)