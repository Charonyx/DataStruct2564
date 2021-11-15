# Title       : Chapter : 15 - item : 4 - Exam_3_4_1a
# Question    : จงเขียนโปรแกรม เพื่อรับข้อมูลแบบ list แล้วนำไปสร้าง BST แบบ height balanced และให้แสดงผลดังตัวอย่าง โดยให้แก้ไขใน ฟังก์ชัน list_to_bst(list_nums) เท่านั้น

# ***หมายเหตุ BST เป็น  Tree ที่ root โหนด มีค่ามากกว่าโหนดทางซ้าย แต่น้อยกว่าโหนดด้านขวา
class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        # self.root = None

def list_to_bst(list_num):
    if not list_num:
        return None
    mid = int(len(list_num) / 2)
    node = TreeNode(list_num[mid])
    node.left = list_to_bst(list_num[:mid])
    node.right = list_to_bst(list_num[mid + 1:])
    return node 
    # for i in list_nums :
        # # node = TreeNode(int(i))
        # node = t.val
        # if t.val == None :
        #     return TreeNode(int(i))
        # else :
        #     _cur = node.val
        #     while _cur != None :
        #         if i < _cur :
        #             if _cur.left == None :
        #                 _cur.left = TreeNode(int(i))
        #                 return node
        #             _cur = _cur.left
        #         else :
        #             if _cur.right == None :
        #                 _cur.right = TreeNode(int(i))
        #                 return node
        #             _cur = _cur.right

def preOrder(node) :
    if not node: 
        return      
    print(str(node.data))
    preOrder(node.left) 
    preOrder(node.right)  

def printBST(node, level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.data)
        printBST(node.left, level + 1)

if __name__ == '__main__' :
    list_nums = sorted([int(item) for item in input("Enter list : ").split()])
    # print(list_nums)
    result = list_to_bst(list_nums)
    # print(result)

    print("\nList to a height balanced BST : ")
    print(preOrder(result))

    print("\nBST model : ")
    printBST(result)

'''
Enter list : 2 3 5 10 203 10 -1 0 -88

List to a height balanced BST : 
3
0
-1
-88
2
10
10
5
203
None

BST model : 
           203
      10
           10
                5
 3
           2
      0
           -1
                -88

'''