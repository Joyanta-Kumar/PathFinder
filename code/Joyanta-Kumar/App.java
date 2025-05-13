import primitive.Edge;
import primitive.Node;

public class App {
    public static void main(String[] args) {
        Node n1 = new Node(0, 0);
        Node n2 = new Node(100, 50);
        Edge e1 = new Edge(n1, n2);

        e1.show();
    }
}