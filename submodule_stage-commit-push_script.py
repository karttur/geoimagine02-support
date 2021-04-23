'''
Created on 12 Feb 2021

@author: thomasgumbricht
'''

# Standard library imports

import os, shutil

import  time

import datetime

def CopyProject():
    ''' Copy project updates to local GitHub clone
    '''
    
    if copyProjectDoc:
        
        pass
    
    else:
        
        for item in submoduleL:
            
            print ("copying updates for package", item)
            
            srcFP = os.path.join(srcProjectFP,item)
    
            files = os.listdir(srcFP)
            
            files.sort()
            
            submoduleGitHubDirName = '%s-%s' %(prefix,item)
            
            dstFP = os.path.join(gitHubFP,submoduleGitHubDirName)
            
            for fn in files:
                
                srcFPN = os.path.join(srcFP, fn)
                
                if not os.path.isfile(srcFPN):
                    
                    continue
                
                if fn in ignoreL:
                    
                    continue
                
                dstFPN =  os.path.join(dstFP, fn)
                
                try:
                    
                    srcTime = datetime.datetime.fromtimestamp( int(os.path.getmtime(srcFPN)) )
                    
                    dstTime = datetime.datetime.fromtimestamp( int(os.path.getmtime(dstFPN)) )
                                        
                    if int( os.stat(srcFPN).st_mtime) <= int(os.stat(dstFPN).st_mtime):

                        continue
                
                except OSError:
                    
                    pass
                
                    print ('error')
                
                print ('    copying', item, fn, dstFPN)
                
                print ('    update created',srcTime, dstTime)
                
                print ('')
                
                shutil.copy(srcFPN, dstFPN) #copying from source to destination

def WriteScript():
    ''' Write script that loops over all the repos and stage, commit and push
    '''
    
    shF = open(scriptFPN, 'w')
    
    for item in submoduleL:
        
        submoduleGitHubDirName = '%s-%s' %(prefix,item)
        
        FP = os.path.join(gitHubFP,submoduleGitHubDirName)
        
        cdCmd = 'cd %s\n' %(FP)
                    
        shF.write(cdCmd)
        
        shF.write('echo "${PWD}"\n')
                    
        stageCmd = 'git add .\n'
        
        shF.write(stageCmd)
        
        commitCmd = 'git commit -m "%s"\n' %(commitMsg)
        
        shF.write(commitCmd)
        
        pushCmd = 'git push origin %s\n' %(branch)
    
        shF.write(pushCmd)
        
        shF.write('\n')
    
    shF.close()
    
    print ('Script file:', scriptFPN)
    
    

if __name__ == "__main__":
    
    copyProject = True
    
    copyProjectDoc = False
    
    branch = 'main'
    
    commitMsg = 'updates apr 2021'
    
    ignoreL = ['__pycache__','.DS_Store']
    
    home = os.path.expanduser('~')
    
    scriptFPN = os.path.join(home, 'submodule_stage_commit_push.sh')
    
    srcProjectFP = '/Users/thomasgumbricht/eclipse-workspace/2020-03_geoimagine/karttur_v202003/geoimagine'
    
    gitHubFP = '/Users/thomasgumbricht/GitHub/'
    
    gitHubAccount = 'karttur'
    
    prefix = 'geoimagine02'
    
    submoduleL = ['ancillary','assets','copernicus',
                  'dem','export',
                  'gis','grace','grass','ktgdal',
                  'ktgrass','ktnumba',
                  'ktpandas','landsat','layout',
                  'modis','npproc',
                  'params','postgresdb','projects',
                  'region','sentinel',
                  'setup_db','setup_processes','smap','support',
                  'timeseries','updatedb','userproj',
                  'zipper']
    
    if copyProject:
        
        CopyProject()
        
    WriteScript()
        


