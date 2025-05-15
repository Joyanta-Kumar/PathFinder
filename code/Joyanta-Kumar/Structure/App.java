import primitive.Edge;
import primitive.Node;
import composition.Graph;

public class App {
    public static void main(String[] args) {
        Node n1 = new Node(0F, 0F);
        Node n2 = new Node(100F, 50F);
        Node n3 = new Node(200F, 100F);
        Edge e1 = new Edge(n1, n2);
        Edge e2 = new Edge(n1, n3);

        Graph graph = new Graph();
        graph.addNode(n1);
        graph.addNode(n2);
        graph.addNode(n3);
        graph.addEdge(e1);
        graph.addEdge(e2);

        graph.show();
    }
}