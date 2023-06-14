import sys
input = sys.stdin.readline
n=int(input())
tree=dict()

for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def pre(root): #root-left-right
    if root!='.':
        print(root,end='')
        pre(tree[root][0])  # left
        pre(tree[root][1])  # right
    
def mid(root): #left-root-right
    if root!='.':
        mid(tree[root][0])  # left
        print(root,end='')
        mid(tree[root][1])  # right
        
def post(root): #left-right-root
    if root!='.':
        post(tree[root][0])  # left
        post(tree[root][1])  # right
        print(root,end='')

pre('A')
print()
mid('A')
print()
post('A')