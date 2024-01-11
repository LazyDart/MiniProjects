
public class Main {
    public static void main(String[] args) {
        Heap h = new Heap(5);
        try {
            h.push(1);
            h.push(2);
            h.push(3);
            h.push(4);



            h.push(5);
            System.out.println(h);
//            h.push(6);

            h.pop();
            h.pop();
            h.pop();
            h.pop();
            h.pop();
//            h.pop();
            System.out.println(h);

        }
        catch (Heap.FullException e) {
            System.out.println("Error 1");
        }
        catch (Heap.EmptyException e) {
            System.out.println("Error 2");
        }

    }
}
