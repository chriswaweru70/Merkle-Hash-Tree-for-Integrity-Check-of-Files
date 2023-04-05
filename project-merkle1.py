import hashlib
import os

def get_file_hash(filename):
    # This is
    hasher = hashlib.sha1()
    #File being opened here
    with open(filename, 'rb') as f:
        while True:
            data = f.read(8192) ## File is read here in chunks of 8192 bytes
            if not data:
                break
            hasher.update(data)  # SHA1 hash object is updated with each chunk of data
    return hasher.hexdigest()

def merkle_tree(files):
    #Computing the hash value of a Merkle hash tree for a list of files
    hashes = [get_file_hash(file) for file in files]
    while len(hashes) > 1:
        hashes = [hashlib.sha1(hashes[i].encode('utf-8') + hashes[i+1].encode('utf-8')).hexdigest() for i in range(0, len(hashes), 2)]
    return hashes[0]

# Example as it works
files = ['L1.txt', 'L2.txt', 'L3.txt', 'L4.txt']
top_hash = merkle_tree(files)
print('Top hash:', top_hash)

# Once one of the files has been Modified compute the top hash again
os.system('echo "Modified content" >> L1.txt')
new_top_hash = merkle_tree(files)
print('New top hash:', new_top_hash)