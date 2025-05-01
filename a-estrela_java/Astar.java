import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

public class Astar{
    
    public static void main(String[] args){
        String arquivo = "C:\\Users\\reich\\OneDrive\\Área de Trabalho\\Ecomp_3ano_2025\\mapa_gerado1.txt";
        int[][] matriz = lerMapa(arquivo);

        //printar mapa
        /*for (int i=0; i < matriz.length;i++){
            for (int j=0; j < matriz[0].length; j++){
                System.out.print(matriz[i][j]);
            }
            System.out.println();
        } */

        Ponto inicio = getLocation(matriz, 2);
        Ponto destino= getLocation(matriz, 3);
        List<Ponto> caminho = aStar(inicio, destino, matriz);

        if (caminho != null) {
            System.out.println("Caminho encontrado:");
            for (Ponto p : caminho) {
                System.out.println("(" + p.x + ", " + p.y + ")");
            }
        } else {
            System.out.println("Nenhum caminho encontrado.");
        }

    }
    
    public static int[][] lerMapa(String arquivo) {
        
        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))){  //abrir arquivo
            //definindo as variaveis
            String linha;
            int linhas = 0;
            int colunas = 0;
        
            //percorrendo o arquivo para iniciar a matriz do tamanho correto
            while ((linha = br.readLine()) != null) {
                linhas++;
                colunas = linha.length();
            }
            int[][] matriz = new int[linhas][colunas];

            br.close();

            BufferedReader br2 = new BufferedReader(new FileReader(arquivo)); //reabrir para ler novamente
            int i = 0;
            while ((linha = br2.readLine()) != null) {
                for (int j = 0; j < linha.length(); j++) {
                    //converter o caractere para o valor inteiro
                    matriz[i][j] = Character.getNumericValue(linha.charAt(j));
                }
                i++;
            }
            br2.close();
            return matriz;

        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static Ponto getLocation(int[][] mapa, int valor){
        for(int i=0; i< mapa.length;i++){
            for(int j=0; j<mapa[0].length;j++){
                if (mapa[i][j] == valor){
                    return new Ponto(i, j);
                }
            }
        }
        return null; 
    }

    public static int heuristica(Ponto nodoAtual, Ponto nodoDestino){
        return Math.abs(nodoAtual.x - nodoDestino.x) + Math.abs(nodoAtual.y - nodoDestino.y);
    }

    public static List<Ponto> getVizinhos(int[][] mapa, Ponto nodoAtual){
        List<Ponto> vizinhos = new ArrayList<>();
        int[][] directions = new int[][] {{1,0}, {-1,0}, {0,1}, {0,-1}};

        for (int i=0; i< directions.length; i++){
            Ponto novo = new Ponto (nodoAtual.x + directions[i][0], nodoAtual.y + directions[i][1]);
            if (novo.x >= 0 && novo.x < mapa.length && novo.y >= 0 && novo.y < mapa[0].length) {
                if (mapa[novo.x][novo.y] != 1) {
                    vizinhos.add(novo);
                }
            }
            
        }
        return vizinhos;
    }

    public static List<Ponto> aStar(Ponto inicio, Ponto destino, int[][] mapa) {
        List<Ponto> aberto= new ArrayList<>();
        aberto.add(inicio);
        Map<Ponto, Ponto> cameFrom = new HashMap<>();
        Map<Ponto, Integer> gScore = new HashMap<>();
        gScore.put(new Ponto(inicio.x, inicio.y), 0);

        Map<Ponto, Integer> fScore = new HashMap<>();
        fScore.put(new Ponto(inicio.x, inicio.y), heuristica(inicio, destino));

        while (!aberto.isEmpty()){
            Ponto melhor = aberto.get(0);
            for (int i = 0; i<aberto.size(); i++){
                if (fScore.get(aberto.get(i)) < fScore.get(melhor)){
                    melhor = aberto.get(i);
                }
            }
            if (melhor.equals(destino)) {
                List<Ponto> caminho = new ArrayList<>();
                caminho.add(melhor);
                while (cameFrom.containsKey(melhor)) {
                    melhor = cameFrom.get(melhor);
                    caminho.add(melhor);
                }
                Collections.reverse(caminho);
                return caminho;
            }
            aberto.remove(melhor);

            List<Ponto> vizinhos = getVizinhos(mapa, melhor);
            for (int i=0; i<vizinhos.size();i++){
                int custo = gScore.get(melhor) + 1;

                if (!gScore.containsKey(vizinhos.get(i)) || custo < gScore.get(vizinhos.get(i))){
                    cameFrom.put(vizinhos.get(i),melhor);
                    gScore.put(vizinhos.get(i), custo);
                    fScore.put(vizinhos.get(i), custo + heuristica(vizinhos.get(i), destino));
                    if (!aberto.contains(vizinhos.get(i))) {
                        aberto.add(vizinhos.get(i));
                    }
                }
            }
        }
        return null;    
    }
}
