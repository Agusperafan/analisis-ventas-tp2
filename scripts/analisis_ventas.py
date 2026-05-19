import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# Descargamos el dataset directamente desde la fuente pública
subprocess.run(['wget', '-O', 'datos/sales_sample_2024.csv', 
    'https://gist.githubusercontent.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6/raw/sales_sample_2024.csv'])

# Leemos el dataset
df = pd.read_csv('datos/sales_sample_2024.csv')

# Convertimos la columna de fecha al tipo datetime
df['sales_date'] = pd.to_datetime(df['sales_date'])

# Extraemos el número de mes de cada fecha
df['mes'] = df['sales_date'].dt.month

# Calculamos indicadores
ventas_totales = df['sales_amount'].sum()
venta_promedio = df['sales_amount'].mean()
venta_maxima = df['sales_amount'].max()
venta_minima = df['sales_amount'].min()
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()
mes_mas_ventas = ventas_por_mes.idxmax()

print('=== INDICADORES DE VENTAS 2024 ===')
print(f'Ventas totales: ${ventas_totales:,.2f}')
print(f'Venta promedio diaria: ${venta_promedio:,.2f}')
print(f'Venta máxima diaria: ${venta_maxima:,.2f}')
print(f'Venta mínima diaria: ${venta_minima:,.2f}')
print(f'Mes con más ventas: {mes_mas_ventas}')

# Graficamos la evolución de ventas mensuales
plt.figure(figsize=(10, 5))
plt.plot(ventas_por_mes.index, ventas_por_mes.values, marker='o', color='mediumseagreen', linewidth=2)
plt.title('Evolución de Ventas Mensuales - 2024')
plt.xlabel('Mes')
plt.ylabel('Total Ventas ($)')
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png')
plt.show()
print('Gráfico guardado en /resultados/grafico_ventas.png')
