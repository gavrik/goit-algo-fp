class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def revers(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def sort(self):
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            if not sorted_head or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                tmp = sorted_head
                while tmp.next and tmp.next.data < current.data:
                    tmp = tmp.next
                current.next = tmp.next
                tmp.next = current
            current = next_node
        self.head = sorted_head


def merge_sorted_lists(list1, list2):
    res = None

    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    if list1.data <= list2.data:
        res = list1
        res.next = merge_sorted_lists(list1.next, list2)
    else:
        res = list2
        res.next = merge_sorted_lists(list1, list2.next)
    return res


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)
llist.insert_at_end(30)
llist.insert_at_end(32)
llist.insert_at_end(3)
llist.insert_at_end(2)
llist.insert_at_end(45)


# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

print("Reversed Linked List")
llist.revers()
llist.print_list()

print("Sorted Linked List")
llist.sort()
llist.print_list()

print("Merged lists")
llist1 = LinkedList()
llist2 = LinkedList()

llist1.insert_at_end(20)
llist1.insert_at_end(25)
llist1.insert_at_end(30)
llist1.insert_at_end(32)
llist1.insert_at_end(3)
llist1.insert_at_end(2)
llist1.insert_at_end(45)
llist1.sort()

llist2.insert_at_end(20)
llist2.insert_at_end(25)
llist2.insert_at_end(30)
llist2.insert_at_end(32)
llist2.insert_at_end(3)
llist2.insert_at_end(2)
llist2.insert_at_end(45)
llist2.sort()

res = merge_sorted_lists(llist1.head, llist2.head)
tmp = res

while tmp:
    print(tmp.data, end=" ")
    tmp = tmp.next

# exit(1)
# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)
