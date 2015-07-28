#template for general purposes
import fileinput
import subprocess
from os import stat
from os import listdir
from os.path import isfile, join
#variable
pathin=''
pathout = ''
file_in_name = ''
file_out_name = ''
des_list = []
def main():
    dict_size  = {}
    mypath = "/home/alizadehlab/bchen45/TCGA/tcga_Andrew/mutationv3/"
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    for x in onlyfiles:
        size0 = stat.
        x2 = x[0:15]
        if not x2 in dic_size:
           x2  
        cmd = ''
        cmd0 = subprocess.Popen(cmd,shell=True)      
        cmd0.wait() 
#         
    file_in = open(pathin+file_in_name,'r')
    file_out = open(pathout+file_out_name,'w+')
    
    file_in.close()
    file_out.close()   
        

if __name__ == '__main__':
    pass

main()


