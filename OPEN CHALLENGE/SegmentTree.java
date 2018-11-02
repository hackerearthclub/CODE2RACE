import java.util.*;

class Solution {
  
  	static void buildTree(int a[], int tree[], int start, int end, int treeNode) {
      if(start == end) {
        tree[treeNode] = a[start];
        return;
      }
      int mid = (start+end)/2;
      buildTree(a, tree, start, mid, 2*treeNode);
      buildTree(a, tree, mid + 1, end, 2*treeNode+1);
      tree[treeNode] = Math.max(tree[2*treeNode], tree[2*treeNode+1]);
    }
  
  	static void update(int a[], int tree[], int start, int end, int treeNode, int idx, int value) {
      if(start == end) {
        a[idx] = value;
        tree[treeNode] = value;
        return;
      }
      int mid = (start + end)/2;
      if(idx > mid) {
        update(a, tree, mid+1, end, 2*treeNode+1, idx, value);
      }
      else {
        update(a, tree, start, mid, 2*treeNode, idx, value);
      }
      tree[treeNode] = Math.max(tree[2*treeNode], tree[2*treeNode + 1]);
    }
  
  	static int query(int tree[], int start, int end, int treeNode, int l, int r) {
      if(end < l || start > r) {
        return 0;
      }
      if(l <= start && end <= r) {
        return tree[treeNode];
      }
      int mid = (start+end)/2;
      int res1 = query(tree, start, mid, 2*treeNode, l, r);
      int res2 = query(tree, mid + 1, end, 2*treeNode + 1, l, r);
      return Math.max(res1, res2);
    }
  
	public static void main(String[] args) {
		// Write your code here
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int q = sc.nextInt();
      int a[] = new int[n];
      int tree[] = new int[4*n];
      for(int i = 0; i < n; i++) a[i] = sc.nextInt();
      buildTree(a, tree, 0, n-1, 1);
      //System.out.println(Arrays.toString(tree));
      while(q-- > 0) {
        sc.nextLine();
        char qu = sc.next().charAt(0);
        int l = sc.nextInt();
        int r = sc.nextInt();
        if(qu == 'q') {
          //System.out.println("0");
          System.out.println(query(tree, 0, n-1, 1, l-1, r-1));
        }
        else {
          update(a, tree, 0, n-1, 1, l-1, r);
          //System.out.println(Arrays.toString(tree));
        }
        //System.out.println(Arrays.toString(tree));
        sc.close();
      }
	}

}

/*
Input:
5 5
1 5 2 4 3
q 1 5
q 1 3
q 3 5
u 3 6
q 1 5
*/
