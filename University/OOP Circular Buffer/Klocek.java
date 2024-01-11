public class Klocek {
    private int l;
    private int r;

    public Klocek (int l, int r){
        this.l = l;
        this.r = r;
    }

    public String toString() {
        return "[" + Integer.toString(l) + ", " + Integer.toString(r) + "]";
    }

    public int getRight() {
        return r;
    }

    public int getLeft(){
        return l;
    }
}
