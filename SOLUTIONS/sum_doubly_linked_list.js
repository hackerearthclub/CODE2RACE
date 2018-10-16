function sumDoublyLinkedList(list, num) {
  let sum = 0;
  let current = list;
  while (current) {
    if (current.value % num === 0) {
      sum = sum + current.value;
    }
    current = current.next;
  }
  return sum;
}
