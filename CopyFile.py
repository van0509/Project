import hashlib
ReadMaxLength=2048

def copyFile(srcFilename,destFilename):
    with open(destFilename,'rb') as fr:
        with open(destFilename,'wb') as fw:
            for i in fr:



def hashFile(filename):
    h=hashlib.sha3_256()

    with open(filename,'rb') as f:
        while True:
            chunk=f.read(ReadMaxLength)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()