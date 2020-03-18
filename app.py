 
import os, sys
import hashlib
 
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
  
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
 
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print(results)
        print('Duplicates Found:') 
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
 
    else:
        print('No duplicate files found.')

def search(path,fileName,parentFolder): 
    print('searching...')
    path = os.path.join(path, fileName)
    hashf=hashfile(path) 
    for i in folders: 
        if os.path.exists(i): 
           filesimilar= findOne(i,hashf)
        else:
            print('%s is not a valid path, please verify' % i)
            sys.exit() 
    return filesimilar

def findOne(parentFolder,hashf):
    # Dups in format {hash:[names]}
    dups = []
    for dirName, subdirs, fileList in os.walk(parentFolder):
        # print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash==hashf: 
            # if file_hash in dups:
                dups.append(path)
            # else:
            #     dups=dups
    return dups

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:] 
        dirNametes='sample'
        filenametes='ori.jpg'
       
        search=search(dirNametes,filenametes,folders)
        print(search)
    else:
        print('Usage: python app.py folder or python app.py folder1 folder2')
