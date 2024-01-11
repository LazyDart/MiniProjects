public class Main {
    public static void main(String[] args) {
        Klocek[] puzzleElements = new Klocek[] {new Klocek(1, 2), new Klocek(3, 4),
                                                new Klocek(5, 6), new Klocek(7, 8)};

        CircularBuffer buffer = new CircularBuffer(puzzleElements);

        System.out.println(buffer.takeElement());
        System.out.println(buffer.takeElement());

        System.out.println(buffer);

        buffer.appendElement(new Klocek(9, 10));
        buffer.appendElement(new Klocek(11, 12));

        System.out.println(buffer);

        System.out.println(buffer.takeElement());

        System.out.println(buffer);

    }
}
