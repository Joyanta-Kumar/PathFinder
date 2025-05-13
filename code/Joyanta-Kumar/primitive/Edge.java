package primitive;

public class Edge {
    Node start;
    Node end;

    public Edge(Node start, Node end) {
        this.start = start;
        this.end = end;
    }

    public void show() {
        this.start.show();
        System.out.println("|");
        this.end.show();
    }
}
