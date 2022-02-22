from traceback import print_stack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        # self.next=None
        

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

################
    
# def intersection(llist1,llist2):

#     if llist1 ==llist2:
#         llist1
            
#     else:
#         if llist1:
#             llist1=llist1.next
#         else:
#             llist2
            
#         if llist2:
#             llist2=llist2.next 
#         else:
#             llist1


############################################3

def intersection(llist1,llist2):

    temp_llist1=[]
    temp_llist2=[]
    if llist1.head is not None:
        temp_llist1.append(llist1.head.value)
        llist1.head=llist1.head.next
    # else:
    #     llist2.head
    
    if llist2.head is not None:
        temp_llist2.append(llist2.head.value)
        llist2.head=llist2.head.next
    

    common=[]
    for x in temp_llist1:
         if x in temp_llist2:
            common.append(x)
            print(common)

    commons=set(common)
    resultant_ll=LinkedList()
    for i in commons:
        resultant_ll.append(i)
        print(resultant_ll)
    return resultant_ll







########################################
    
# def union(llist1,llist2):

#     if llist1  ==llist2 :
#         return llist1
        
#     else:
#         if llist1:
#             return llist1
#         else:
#             llist2

######################################

def union(llist1,llist2):
    if llist1.head is None and llist2.head is None:
        return None
    
    result=[]
    if llist1.head is not None :
        result.append(llist1.head.value)
    else:
        result.append(llist2.head.value)
    
    final_result=set(result)

    final_ll=LinkedList()
    for result in final_result:
        final_ll.append(result)
        print(final_ll)
    
    return final_ll





## Test case 1


linked_list1=LinkedList()
linked_list2=LinkedList()

elemnent1=[3,2,4,35,6,65,6,4,3,21]
elemnent2=[6,32,4,9,1,11,21,1]

for i in elemnent1:
    linked_list1.append(i)

for i in elemnent2:
    linked_list2.append(i)

print(linked_list1)
print(linked_list2)
print("#############")
print(union(linked_list1,linked_list2))
print(intersection(linked_list1,linked_list2))

    
         

### test case 2
print("##########################")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3)
print(linked_list_4)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


