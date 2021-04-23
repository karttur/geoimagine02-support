'''
Created on 24 Mar 2021

@author: thomasgumbricht

Tilefit is a script for finding corner points defining arbitrary region that fit the 
predefined systems of Kartturs GeoImagine Framework
'''

import json


def js_r(filename: str):
    
    with open(filename) as f_in:
        
        return json.load(f_in)
    
def FindMin(edge,coord,resol):
    
    cells = (coord-edge)/resol
    
    minimum = edge + int(cells)*resol
    
    return minimum

def FindMax(minimum,coord,resol):
    
    cells = (coord-minimum)/resol
    
    maximum = minimum + int(cells)*resol
    
    return maximum

def AdjustDimDiv(dimdiv,x0,y0,xres,yres,llx,lly,urx,ury):
    
    x = 0
    
    while True:
        
        xdim = (urx-llx)/xres
                    
        if xdim % dimdiv == 0:
            
            break
        
        if x % 2 == 0:
            
            urx += xres
            
        elif llx-xdim >= x0:
            
            llx -= xres
            
        x +=1
       
    y = 0
     
    while True:
        
        ydim = (ury-lly)/yres
                    
        if ydim % dimdiv == 0:
            
            break
        
        if y % 2 == 0:
            
            ury += yres
            
        elif lly-ydim >= y0:
            
            lly -= yres
            
        y +=1
        
    return (llx,lly,urx,ury)


def FindRegion(jsonFPN):
    
    regionD = js_r(jsonFPN)
    
    print (regionD)
    
    for system in regionD:
        
        print ('system',system)
        
        for reg in regionD[system]:
            
            print ('    region:', reg['regionid'])
            
            dimdiv = reg['dimdiv']
            
            x0 = reg['x0']
            
            y0 = reg['y0']
            
            xres = reg['xres']
            
            yres = reg['yres']
            
            minx = reg['minx']
            
            miny = reg['miny']
            
            maxx = reg['maxx']
            
            maxy = reg['maxy']
            
            llx = FindMin(x0,minx,xres)
            
            lly = FindMin(y0,miny,yres)
            
            urx = FindMax(llx,maxx,xres)
            
            ury = FindMax(lly,maxy,yres)
            
            xdim = (urx-llx)/xres
            
            ydim = (ury-lly)/yres
            
            infostr = '        input: minx: %s, miny: %s maxx: %s, maxy: %s' %(minx,miny,maxx,maxy)

            print (infostr)
            
            infostr = '        initial: minx: %s, miny: %s maxx: %s, maxy: %s, xdim: %s, ydim: %s' %(llx,lly,urx,ury,xdim,ydim)
            
            print (infostr)
            
            llx,lly,urx,ury = AdjustDimDiv(dimdiv,x0,y0,xres,yres,llx,lly,urx,ury)
            
            xdim = (urx-llx)/xres
            
            ydim = (ury-lly)/yres
            
            infostr = '        adjusted: minx: %s, miny: %s maxx: %s, maxy: %s, xdim: %s, ydim: %s' %(llx,lly,urx,ury,xdim,ydim)

            print (infostr)
            
            

if __name__ == "__main__":
    
    jsonFPN = 'doc/hydroregion_setup.json'
    
    FindRegion(jsonFPN)
    
    
    
    
    