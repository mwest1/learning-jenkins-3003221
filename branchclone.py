#!/usr/bin/env python3

import subprocess

def getInventory():
    # cmd = "git branch -r"
    RemoteBranches = subprocess.run(['git','branch','-r'], capture_output=True, text=True).stdout
    # this will create a single string must split this based on whitespaces
    BranchList = RemoteBranches.split()
    
    return(BranchList)
 
def CloneRemoteBranch(RemoteBranches):
    for item in RemoteBranches:
        if "origin" in item:
            # extract the local branch name by removing the "origin/"
            localBranch = item.split('/')[1]

            # run the folllowing command :
            # git checkout -b 01_04 origin/01_04
            try:
                subprocess.run(['git','checkout','-b',localBranch,item])
            except:
                continue
            



def main (): 

# read in the inventory 
    RemoteBranches = getInventory()
    CloneRemoteBranch(RemoteBranches)

if __name__ == "__main__":
    main()

