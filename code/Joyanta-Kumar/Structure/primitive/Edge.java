package primitive;

import utils.Calculation;

public class Edge {
    Node start;
    Node end;

    public Edge(Node start, Node end) {
        this.start = start;
        this.end = end;
    }

    public void show() {
        System.out.print("[" + this.start.getX() + "," + this.start.getY() + "]");
        System.out.print(" --- ");
        System.out.println("[" + this.end.getX() + "," + this.end.getY() + "]");
    }

    public float getLength() {
        return Calculation.getDistance(this.start, this.end);
    }
}
