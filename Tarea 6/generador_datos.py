import pandas as pd
import random

def generar_datos_entrenamiento(num_filas=1000):
    datos = []
    for _ in range(num_filas):
        # 1. Generar variables aleatorias de entrada en sus rangos válidos
        T = random.randint(0, 40)
        H = random.randint(0, 2)
        L = random.randint(0, 1000)
        Hum = random.randint(0, 100)
        
        # 2. Reglas de Temperatura para Resistencia y Ventilador
        if T < 5:
            res = 2
            ven_t = 0
        elif 5 <= T <= 15:
            res = 1 if H == 1 else 0 # Se activa a media potencia solo de día
            ven_t = 0
        elif 16 <= T <= 21:
            res = 1 if H == 1 else 0
            ven_t = 1
        else: # T >= 22
            res = 0
            ven_t = 2
            
        # 3. Reglas de Humedad para Ventilador y Humidificador
        if Hum < 40:
            humid = 1
            ven_h = 0
        elif 40 <= Hum <= 70:
            humid = 0
            ven_h = 0
        else: # Hum > 70
            humid = 0
            ven_h = 1
            
        # 4. Resolución de conflicto: Gana quien pida mayor nivel de ventilación
        ven = max(ven_t, ven_h)
        
        # 5. Reglas de Luminosidad y Hora para Persianas y Luces
        if H == 0 or H == 2: # Mañana o Noche
            per = 0
            luc = 0
        else: # Día (H == 1)
            if L <= 300:
                per = 2
                luc = 1
            elif 301 <= L <= 700:
                per = 1
                luc = 0
            else: # L > 700
                per = 0
                luc = 0
                
        datos.append([T, H, L, Hum, res, ven, per, luc, humid])
        
    # Crear y exportar el DataFrame
    columnas = ['Temperatura', 'Hora', 'Luminosidad', 'Humedad', 
                'Resistencia', 'Ventilador', 'Persianas', 'Luces', 'Humidificador']
    df = pd.DataFrame(datos, columns=columnas)
    
    return df

# Generar 1000 estados y exportar a CSV
df_entrenamiento = generar_datos_entrenamiento(1000)
df_entrenamiento.to_csv("dataset_invernadero.csv", index=False)
print("¡Archivo dataset_invernadero.csv con 1000 registros generado exitosamente!")