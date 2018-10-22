function sumDoublyLinkedList(list: {value: number, next: Object }, num: number) {
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
