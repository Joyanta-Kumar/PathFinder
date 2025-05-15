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
        System.out.println("{");
        System.out.print("\t\t");
        this.start.show();
        System.out.print(",\n\t\t");
        this.end.show();
        System.out.print("\n\t}");
    }

    public float getLength() {
        return Calculation.getDistance(this.start, this.end);
    }
}
