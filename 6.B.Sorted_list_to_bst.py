
class node(object):

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def sort_list_to_bst(lst, start, end):

    if start == end:
        return node(lst[start])

    mid_idx = (start + end) // 2
    value = lst[mid_idx]


    if mid_idx == end:
        return node(lst[end])
    elif start == mid_idx:
        return node(lst[start])
    else:
        return node(value, sort_list_to_bst(lst, start, mid_idx - 1), sort_list_to_bst(lst, mid_idx + 1, end))



def scan(node):

    if not node:
        return
    scan(node.left)
    print(node.value)
    scan(node.right)


def sort(lst):

    lst = sorted(lst)
    return sort_list_to_bst(lst, 0, len(lst) - 1)




def main():
    node = sort([1,2,3,4,5,6,7])
    scan(node)





if __name__ == '__main__':
    main()