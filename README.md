# Hundir la flota

Juego de consola en Python contra un bot. Cada participante tiene un tablero de 10 × 10 y una flota de seis barcos: uno de 4 casillas, dos de 3 y tres de 2. Los barcos se colocan al azar sin tocarse entre sí.

## Cómo jugar

Instala NumPy y ejecuta el programa desde esta carpeta:

```bash
pip install numpy
python main.py
```

Introduce cara o cruz y el programa sorteará quién empieza. Cuando sea tu turno, escribe dos dígitos seguidos: el primero es la fila y el segundo la columna. Por ejemplo, `35` dispara a la fila 3, columna 5. Un acierto se marca con `4` y el agua con `0`. Si aciertas, sigues jugando; si fallas, pasa el turno. Gana quien alcance primero las 16 casillas de la flota rival.

`main.py` inicia la partida, `funciones.py` contiene las reglas y `variables.py` define las esloras. Por ahora, `main.py` muestra las coordenadas de ambas flotas para facilitar las pruebas; quita esos dos `print` para jugar sin ver la solución.
