import sys

n = int(sys.stdin.readline())  
tree = dict()  # 트리 생성

# 트리 입력
for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = (left, right)  # 루트 노드의 왼쪽, 오른쪽 자식을 저장


# 전위 순회
def preorder(v):
    if v != ".":  # 현재 노드가 유효하다면
        print(v, end="")  # 현재 노드 출력
        preorder(tree[v][0])  # 왼쪽 자식 탐색
        preorder(tree[v][1])  # 오른쪽 자식 탐색


# 중위 순회
def inorder(v):
    if v != ".":  # 현재 노드가 유효하다면
        inorder(tree[v][0])  # 왼쪽 자식 탐색
        print(v, end="")  # 현재 노드 출력
        inorder(tree[v][1])  # 오른쪽 자식 탐색


# 후위 순회
def postorder(v):
    if v != ".":  # 현재 노드가 유효하다면
        postorder(tree[v][0])  # 왼쪽 자식 탐색
        postorder(tree[v][1])  # 오른쪽 자식 탐색
        print(v, end="")  # 현재 노드 출력


preorder('A') 
print()
inorder('A')  
print()
postorder('A')  
