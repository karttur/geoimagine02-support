'''
Created on 27 apr. 2018

@author: thomasgumbricht
'''

# Package application imports

from geoimagine.support import karttur_dt as mj_dt

def ConvertXYstring(xy):
    ''' Convert EASE grid xtile / ytile to a standardized string
    '''
    if xy[0] < 10:
        pathStr = 'x0%(x)d' %{'x': xy[0]}
    else:
        pathStr = 'x%(x)d' %{'x': xy[0]}
        
    if xy[1] < 10:
        rowStr = 'y0%(y)d' %{'y': xy[1]}
    else:
        rowStr = 'y%(y)d' %{'y': xy[1]}
    pathrowStr = '%(x)s%(y)s' %{'x':pathStr,'y':rowStr}
    values = [xy[0], xy[1], pathStr, rowStr, pathrowStr]
    params = ['p','r','pstr','rstr','prstr']
    D = dict(zip(params,values))
    return D

def ConvertXYinteger(x,y):
    ''' Convert EASEGRID xtile / ytile to a standardized string
    '''
    if x < 10:
        pathStr = 'x0%(x)d' %{'x': x}
    else:
        pathStr = 'x%(x)d' %{'x': x}
    if y < 10:
        rowStr = 'y0%(y)d' %{'y': y}
    else:
        rowStr = 'y%(y)d' %{'y': y}
        
    pathrowStr = '%(x)s%(y)s' %{'x':pathStr,'y':rowStr}
    
    values = [x, y, pathStr, rowStr, pathrowStr]
    
    params = ['p','r','pstr','rstr','prstr']
    
    D = dict(zip(params,values))
    
    return D
    
    
            
    
