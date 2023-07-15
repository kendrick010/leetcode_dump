def addTwoNumbers(l1, l2):
    carry = 0
    root = temp = ListNode(val=0)

    while l1 or l2 or carry:
        temp.val += carry
        if l1:
            temp.val += l1.val
            l1 = l1.next

        if l2:
            temp.val += l2.val
            l2 = l2.next

        carry = temp.val // 10
        temp.val -= 10 * carry

        if l1 or l2 or carry > 0:
            temp.next = ListNode(val=0)
            temp = temp.next

    return root