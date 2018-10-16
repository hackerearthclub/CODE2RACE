import java.util.*;
import java.lang.*;
import java.util.regex.*;

class Node {
    private int data;
    private Node left;
    private Node right;

    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public void setRight(Node right) {
        this.right = right;
    }

    public void setData(int data) {
        this.data = data;
    }

    public int getData() {
        return data;
    }

    public Node getLeft() {
        return left;
    }

    public Node getRight() {
        return right;
    }

}

class DLL {

    private Node head;

    public DLL() {
        this.head = null;
    }

    public Node getHead() {
        return head;
    }

    public void setHead(Node head) {
        this.head = head;
    }

}

class sumDoublyLinkedList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputDLLS = sc.nextLine();

        // this pattern matcher extracts the numbers from the list
        Pattern p = Pattern.compile("\\b\\d+\\b");
        Matcher m = p.matcher(inputDLLS);

        DLL newDLL = new DLL();
        Node ptr = null;

        while (m.find()) {
            int newElement = Integer.parseInt(m.group());
            Node newNode = new Node(newElement);

            if (newDLL.getHead() == null) {
                newDLL.setHead(newNode);
                ptr = newDLL.getHead();
            } else {
                ptr.setRight(newNode);
                newNode.setLeft(ptr);
                ptr = newNode;
            }
        }

        String inputParams = sc.nextLine();
        p = Pattern.compile("\\d+");
        int divideElement = -1;
        m = p.matcher(inputParams);
        if (m.find()) {
            divideElement = Integer.parseInt(m.group());
        }

        int totalSum = 0;

        ptr = newDLL.getHead();
        while (ptr.getRight() != null) {
            if (ptr.getData() % divideElement == 0)
                totalSum += ptr.getData();
            ptr = ptr.getRight();
        }

        System.out.println("Sum = " + totalSum);
    }
}