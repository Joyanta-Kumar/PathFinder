import primitive.Edge;
import primitive.Node;
import utils.Calculation;

public class App {
    public static void main(String[] args) {
        Node n1 = new Node(0F, 0F);
        Node n2 = new Node(100F, 50F);
        Edge e1 = new Edge(n1, n2);

        System.out.println(e1.getLength());
    }
}