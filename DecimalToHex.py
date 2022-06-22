def getHexValue( x ):
    H = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    hexValue = ""
    
    while x != 0:
        q = int(x/16)
        r = x % 16
        hexValue = H[r] + hexValue
        x = q   

    if hexValue == "":
        return "00"

    elif len(hexValue) == 1:
        return "0" + hexValue

    else:
        return hexValue

def getPythonColor(r, g, b):
    rHex = getHexValue( r )
    gHex = getHexValue( g )
    bHex = getHexValue( b )
    color = "#" + rHex + gHex + bHex
    return color
