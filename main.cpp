#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

// Archivo global
ofstream outfile("lines.txt");

// Función recursiva para la curva de Koch
void koch(double x1, double y1, double x2, double y2, int depth) {
    if (depth == 0) {
        // Caso base: simplemente escribimos el segmento
        outfile << "(" << (int)x1 << "," << (int)y1 << ")"
                << "(" << (int)x2 << "," << (int)y2 << ")\n";
    } else {
        // Dividimos el segmento en 3 partes
        double dx = (x2 - x1) / 3.0;
        double dy = (y2 - y1) / 3.0;

        // Puntos intermedios
        double xA = x1 + dx;
        double yA = y1 + dy;

        double xB = x1 + 2 * dx;
        double yB = y1 + 2 * dy;

        // Pico (punto del triángulo equilátero)
        double xPeak = (xA + xB) / 2 - sqrt(3.0) * (yB - yA) / 2;
        double yPeak = (yA + yB) / 2 + sqrt(3.0) * (xB - xA) / 2;

        // Llamadas recursivas, se manda a llamar 4 veces porque se crean 4 segmentos, cada uno con profundidad reducida
        // La profundidad quiere decir cuántas veces se va a dividir el segmento, en este caso se divide en 3 partes y se agrega un pico, por lo que se llama 4 veces
        koch(x1, y1, xA, yA, depth - 1);
        koch(xA, yA, xPeak, yPeak, depth - 1);
        koch(xPeak, yPeak, xB, yB, depth - 1);
        koch(xB, yB, x2, y2, depth - 1);
    }
}

int main(int argc, char* argv[]) {
    if (argc != 6) {
        cerr << "Uso: " << argv[0] << " <depth> <x1> <y1> <x2> <y2>\n";
        cerr << "Ejemplo: " << argv[0] << " 4 100 500 900 500\n";
        return 1;
    }

    int depth = stoi(argv[1]);
    double x1 = stod(argv[2]);
    double y1 = stod(argv[3]);
    double x2 = stod(argv[4]);
    double y2 = stod(argv[5]);

    // Limpiamos archivo antes de escribir
    outfile.open("lines.txt", ios::trunc);
    outfile.close();
    outfile.open("lines.txt");

    // Llamamos a la recursión
    koch(x1, y1, x2, y2, depth);

    outfile.close();
    cout << "Archivo lines.txt generado correctamente\n";
    return 0;
}
