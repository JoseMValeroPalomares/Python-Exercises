import matplotlib.pyplot as plt

def dibujar_rombo():
    # Definir los puntos del rombo
    x = [0, 1, 2, 1, 0]
    y = [1, 0, 1, 2, 1]

    # Configurar el gráfico
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim([-1, 3])
    ax.set_ylim([-1, 3])

    # Dibujar el rombo
    ax.plot(x, y, color='black')
    ax.fill(x, y, color='gray')

    # Mostrar el gráfico
    plt.show()

# Llamar a la función para dibujar el rombo
dibujar_rombo()