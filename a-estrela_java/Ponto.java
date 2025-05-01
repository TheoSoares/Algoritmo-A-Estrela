import java.util.Objects;

public class Ponto {
    int x;int y;

    public Ponto(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Ponto)) return false;
        Ponto p = (Ponto) o;
        return x == p.x && y == p.y;
    }
    public int hashCode() {
        return Objects.hash(x, y);
    }
}
