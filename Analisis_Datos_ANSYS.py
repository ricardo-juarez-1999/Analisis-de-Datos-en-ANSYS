import os
os.system("cls")
import pandas as pd
import matplotlib.pyplot as plt

archivo = "C:/Python/ANSYS_Data/Reposho_Bueno.csv"

archi = pd.read_csv(archivo, skiprows=6)
## Buscar la manera de realizar el proceso de Renombrar mucho más facil y rapido ##
archi = archi.rename(columns={
    "P1": "Velocidad [m/s]",
    "P2": "Delta_P [Pa]",
    "P7": "Cortante [Pa]",
    "P8": "Factor_Friccion",
    "P12": "Reynolds",
    "P13": "Nusselt"
})

print()
# La variable de esta lista puede adaptarse a cualquiera de las variables dentro del archivo CSV
# Descomentar las siguientes lineas muestra la lista de Reynolds
#print("Esta es la lista de Reynolds")
lista_Rey = archi["Reynolds"].tolist()
#print(lista_Rey)
#print()

#print()
# La variable de esta lista puede adaptarse a cualquiera de las variables dentro del archivo CSV
# Descomentar las siguientes lineas muestra la lista de Nusselt
#print("Esta es la lista de Nusselt")
lista_Nu = archi["Nusselt"].tolist()
#print(lista_Nu)
#print()

print(archi)
print()

# Configuración de la Grafica
plt.figure(figsize=(10,6))

# Linea principal
plt.plot(
    lista_Rey,
    lista_Nu,
    marker = 'o',
    linestyle = '-',
    linewidth = '2',
    markersize = '7',
    label = 'Datos de Simulación'
)

# Etiquetas
plt.xlabel('Reynolds', fontsize = 14)
plt.ylabel('Nusselt', fontsize = 14)

# Titulo
plt.title('Grafica de Simulación', fontsize = 17)

# Cuadricula tipo paper
plt.grid(True, linestyle = '--', alpha = 0.6)

# Leyenda
plt.legend(fontsize = 12)

# Ajuste de Margenes
plt.tight_layout()

## Descomentar la siguiente línea si se requiere guardar la imagen automáticamente:
# plt.savefig('comparacion_graficas.png', dpi=300)

# Mostrar grafica
plt.show()

