# -*- coding:utf-8 -*-
'''
@project=爬虫
@file=深度优先与广度优先的遍历算法
@Author=Administrator
@creat_time=2018/8/1515:55
'''

'''深度优先：

    将一个子节点的所有内容全部遍历完毕之后再去遍历其他节点实现的 （递归实现）

上面的树通过深度优先遍历出来的结果是:  A-->B-->D-->E-->I-->C-->F-->G-->H

使用python语言编写的代码如下:'''


def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node._data)
        if tree_node._left is None:
            return depth_tree(tree_node._left)
        if tree_node._right is None:
            return depth_tree(tree_node._right)


'''广度优先:

   广度优先的算法的实现是通过 分层次的进行遍历 先遍历第一层，然后第二层，第三层 (队列实现)

  上面的树通过深度优先遍历出来的结果是:   A-->B-->C-->D-->E-->F-->F-->G-->H'''


def level_queue(root):
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchild is None:
            my_queue.append(node.lchild)
        if node.rchild is None:
            my_queue.append(node.rchild)

''''''
