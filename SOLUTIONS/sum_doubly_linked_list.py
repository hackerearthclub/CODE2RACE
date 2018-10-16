def dll_sum(head, k):
    sum_ = 0
    while head:
        if head.val % k == 0:
            sum_ += head.val
        head = head.next
    return sum_
