public class CircularBuffer<T> {
    private int start;
    private int end;
    private T[] elements;
    private int size;

    public CircularBuffer(T [] elementArr) {
        elements = new T[elementArr.length];

        for (int i = 0; i < elementArr.length; i++) {
            elements[i] = elementArr[i];
        }
        start = 0;
        end = 0;
        size = elements.length;
    }

    public CircularBuffer(CircularBuffer copyBuffer) {
        elements = new T[copyBuffer.getSize()];

        int copyStart = copyBuffer.getStart();
        for (int i = 0; i < elements.length; i++) {
            elements[i] = copyBuffer.getithElement((copyStart + i) % copyBuffer.getSize());
        }

        start = 0;
        end = 0;
        size = elements.length;

    }

    public T takeElement() {
        T element = elements[start];
        elements[start] = null;
        start += 1;
        start = start % size;


        return element;
    }

    public void appendElement(T element) {
        assert elements[end] == null: "Value cannot be appended, no empty space!";

        elements[end] = element;
        end += 1;
        end = end % size;
    }

    public String toString() {
        String returnString = "[";

        for (T element: elements) {
            if (element != null) {
                returnString += element.toString() + ", ";
            }
            else {
                returnString += "[,], ";
            }
        }

        return returnString + "]";
    }

    public int getSize() {
        return size;
    }

    public int getStart() {
        return start;
    }

    public T getithElement(int i) {
        assert ((i > 0) && (i < size)): "Invalid Index!";
        return elements[i];
    }
}
