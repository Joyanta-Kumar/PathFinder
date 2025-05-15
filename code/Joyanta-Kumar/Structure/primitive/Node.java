package primitive;

public class Node {
    private float x;
    private float y;

    public Node(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float getX() { return this.x; }
    public float getY() { return this.y; }

    public void show() {
        System.out.print("{" + this.x + ", " + this.y + "}");
    }
}
