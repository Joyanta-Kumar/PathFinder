package utils;

import primitive.Node;

public class Calculation {
    public static float getDistance(Node start, Node end) {
        return (float) Math.hypot(start.getX() - end.getX(), start.getY() - end.getY());
    }
}
