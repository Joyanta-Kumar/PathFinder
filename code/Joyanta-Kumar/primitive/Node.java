package primitive;

public class Node {
    int x;
    int y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void show() {
        System.out.println("[" + this.x + ",\t" + this.y + "]");
    }
}
