import os

pre='5'
l=1
r=7


for i in range(l,r):
    if not os.path.exists(f'{pre}.{i}'):
        os.makedirs(f'{pre}.{i}')