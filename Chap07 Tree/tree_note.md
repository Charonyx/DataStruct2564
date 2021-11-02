=== Tree ===
>> Tree Terminalogy
    - โครงสร้างข้อมูลเป็น Hierarchy
        Hierarchy: เป็นลำดับชั้นของข้อมูลที่ใช้ในการแบ่งโครงสร้างต่าง
    - มาบริหารจัดการข้อมูลให้เป็นระบบมากขึ้น ใช้ในการ Searching สามารถเก็บเป็น path ต่างๆที่ใช้เก็บ 
    - ex. file system (/user/root/meow/...)


             _________[A]_________              Tree: 11 Node, 10 Edge
             ↓                   ↓              Root: in any tree the first node is called as "root node"
     _______[B]_______        __[C]__               [A]       
     ↓       ↓       ↓        ↓     ↓           Edge/Branch/Link: in any tree, "Edge" is a  connecting link between node           
    [D]   __[E]__   [F]      [G]   [H]              10 Edge
          ↓     ↓             ↓                 Parent: Node ที่มี Outdegree
         [I]   [J]           [K]                    [A], [B], [C], [E], [G]

    Child: Node ที่มี Indegree
        [B], [C] are children of [A]
        [D], [E], [F] are children of [B]
        [G], [H] are children of [C]
        [I], [J] are children of [E]
        [K] is children of [G]

    Siblings: พี่น้อง, in any tree the nodes which has same parent are called "Siblings"
        [B], [C]
        [D], [E], [F]
        [G], [H]
        [I], [J]

    Leaf/External Node: Node ที่มี Outdegree = 0 หรือ Node ล่างสุด, a node without successors is called "Leaf" node
        [D], [I], [J], [F], [K], [H]

    Internal Nodes: != Root, Leaf หรือ Node ที่อยู่ระหว่างกลาง
        [B], [C], [E], [G]

    Degree: มีกี่ลูก? in any tree, "Degree" a node is total number of children is has
        Indegree: (Edge ที่เข้าหา Node)
        Outdegree: (Edge ที่ออกหา Node)

        Degree of [A] is 2
        Degree of [B] is 3
        Degree of [F] is 0

    Level: ระยะห่างจาก root โดยให้ root เป็น "0"
    Height: Level สูงสุดของ Leaf + 1 โดยไล่จากล่างขี้นบน, in any tree, "Height of Node" is total number of Edge from leaf tp that node in longest path
        [A] Height is 3
        [B], [C] Height is 2
        [I], [J], [K] Height is 0

    Depth: นับจากบนลงล่าง ให้ root เป็น "0" เสมอ, in any tree, "Depth of Node" is total number of Edge from root to that leafnode
        [A] Depth is 0
        [B], [C] Depth is 1

    Path: เส้นทางระหว่าง 2 Node เป็น sequence, in any tree, "Path" is a sequence of nodes and edges between two nodes
        [A] -> [J]: [A] -> [B] -> [E] -> [K]

    Subtree: เป็น Tree ย่อยของ Tree ใหญ่

    Ancester: (บรรพบุรุษ) ทุก Node ในเส้นทางจาก Root -> Node
        Ancester of [G]: [A], [C]
    Descendent: (ลูกหลาน) ทุก Node ในเส้นทางไปยัง Leaf
        Descendent of [A]: ทุก Node จากแผนภาพยกเว้น [A]


>> Binary Tree: Tree ที่มี Subtree ได้ไม่เกิน 2 Subtree (Left Subtree, Right Subtree)
    - Perfect Binary Tree: คือ Tree ที่มีทั้งซ้ายและขวาครบถ้วน

    Arrays Tree: 

                ______________[1]____________
                ↓                           ↓
        ______[2]_______             ______[3]______
        ↓              ↓             ↓             ↓
      __[4]__       __[5]__       __[6]__       __[7]__
      ↓     ↓       ↓     ↓       ↓     ↓       ↓     ↓
     [8]   [9]   [10]   [11]   [12]   [13]   [14]   [15]

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
     1|    2|          3|                            4|

    Linklist: 
    [Left Child Address | Data | Right Child Address]
    ถ้าไม่มี Node ลูกขึ้นเป็น Null


CR. Jeremy CRUNZEX ;P