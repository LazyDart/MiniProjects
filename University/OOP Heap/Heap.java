public class Heap {
    private int size;
    private int lastIndex;
    public int[] data;

    public class FullException extends Exception{
    }
    public class EmptyException extends Exception{
    }

    public Heap(int size) {
        this.size = size;
        this.data = new int[size];
        lastIndex = -1;
    }

    public Heap(int[] data) {
        this.data = new int[data.length];
        this.size = data.length;

        for (int i = 0; i < this.size; i++) {
            this.data[i] = data[i];
        }
        this.lastIndex = size - 1;
    }

    public String toString() {
        if (lastIndex == -1) {
            return "[]";
        }
        String returnString = "[";
        for (int i=0; i < lastIndex; i++) {
            returnString += Integer.toString(data[i]) + ", ";
        }
        returnString += Integer.toString(data[lastIndex]);

        return returnString + "]";
    }

    public void push(int element) throws FullException {
        if (lastIndex + 1 == size) throw new FullException();
        data[lastIndex + 1] = element;
        lastIndex += 1;
    }

    public int pop() throws EmptyException {
        if (lastIndex == -1) throw new EmptyException();
        lastIndex -= 1;
        return data[lastIndex + 1];
    }

}
