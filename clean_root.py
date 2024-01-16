import os

def rmtree(top):
    os.rmdir(top)

if __name__ == "__main__":
    print('Removing /lib/ ...')
    rmtree('lib/')
    print('Removing /src/ ...')
    rmtree('src/')
    os.remove('./clean_root.py')
