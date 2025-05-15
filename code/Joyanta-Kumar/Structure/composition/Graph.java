package composition;

import java.util.ArrayList;
import primitive.Edge;
import primitive.Node;

public class Graph {
    ArrayList<Node> nodes = new ArrayList<Node>();
    ArrayList<Edge> edges = new ArrayList<Edge>();

    public void show() {
        System.out.println("\"Nodes\": [");
        for (Node node : nodes) {
            System.out.print("\t");
            node.show();
            if (node != this.nodes.getLast()) {
                System.out.print(",");
            }
            System.out.println();
        }
        System.out.println("]");

        System.out.println("\"Edges\": [");
        for (Edge edge : edges) {
            System.out.print("\t");
            edge.show();
            if (edge != this.edges.getLast()) {
                System.out.print(",");
            }
            System.out.println();
        }
        System.out.println("]");
    }

    public void addNode(Node node) {
        this.nodes.add(node);
    }

    public void addEdge(Edge edge) {
        this.edges.add(edge);
    }
}
