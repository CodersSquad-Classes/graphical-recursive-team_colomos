# Makefile simple para Koch Curve Generator
# Compilador
CXX = g++

# Flags de compilación
CXXFLAGS = -Wall -Wextra -std=c++17

# Nombre del ejecutable
TARGET = koch_curve

# Archivo fuente
SOURCE = main.cpp

# Regla por defecto
all: $(TARGET)

# Compilar el programa
$(TARGET): $(SOURCE)
	$(CXX) $(CXXFLAGS) $(SOURCE) -o $(TARGET)

# Limpiar archivos generados
clean:
	rm -f $(TARGET) a.out lines.txt

# Ejecutar con parámetros de ejemplo
run:
	./$(TARGET) 3 100 500 900 500

# Visualizar resultado
show:
	python3 graph_generator.py

# Compilar y ejecutar todo
demo: $(TARGET) run show

.PHONY: all clean run show demo
