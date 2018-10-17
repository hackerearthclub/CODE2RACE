/*
 struct Node {
  int data;
  struct *Node next;
  struct *node prev;
  }
  */
  
  
  int addKDivisibleNode(struct Node *node , int k){
    int sum=0;
    while(node!=NULL){
      if(node->data % k == 0)
        sum=sum+node->data;
      node=node->next;  
    }
    return sum;
  }
