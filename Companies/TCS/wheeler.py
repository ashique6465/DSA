def findTwoandFour_wheeler(V,W):
    if(4*V - W) % 2 != 0 or W%2 !=0 or 4*V<W or 2*V>W:
        return "Invalid"
    FW= (W-2*V)//2
    TW = V-FW
    return TW,FW
        
    


V = 200
W = 540
result = findTwoandFour_wheeler(V,W)
if isinstance(result,tuple):
    TW,FW = result
    print(f"TW = {TW},FW = {FW}")
else:
    print(result)