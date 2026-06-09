class LinkedList {
    class Node{
        Node next;
        int data;

        Node(int val){
            next = null;
            data = val;
        }
    }

    Node head;
    Node tail;

    public LinkedList() {
        head = new Node(0); // dummy head
        tail = head;
    }

    public int get(int index) {
        int i = 0;
        Node curr = head.next;
        while(curr != null && i < index){
            i++;
            curr = curr.next;     
        }
        return (curr == null)? -1 : curr.data;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = head.next;
        head.next = newNode;
        if(newNode.next == null)
            tail = newNode;
    }

    public void insertTail(int val) {
        tail.next = new Node(val);
        tail = tail.next;
        //this.tail.next = new Node(val);
        //this.tail = this.tail.next;
        /*Node curr = head.next;
        while(curr.next != null)
            curr = curr.next;
        curr.next = new Node(val);*/
    }

    public boolean remove(int index) {
        int i = 0;
        Node curr = head;
        while(curr != null && i < index){
            i++;
            curr = curr.next;
        }

        if(curr != null && curr.next != null){
            if(curr.next == tail)
                tail = curr;
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> list = new ArrayList<>();
        for(Node curr = head.next; curr != null; curr = curr.next)
            list.add(curr.data);
        return list;
    }
}
