# Proyecto_Sprint_7
# Aplicación Streamlit: Análisis de Vehículos Usados

Esta aplicación web interactiva permite explorar un conjunto de datos de anuncios de venta de vehículos en EE.UU.

## Funcionalidad

- **Histograma interactivo** para visualizar la distribución del kilometraje (`odometer`) de los vehículos.
- **Gráfico de dispersión** para analizar la relación entre el año del modelo (`model_year`) y el precio (`price`).
- Controles dinámicos mediante **botones** 

## Estructura

Proyecto_Sprint_7/
- vehicles_us.csv # Archivo de datos
- notebooks/
    - EDA.ipynb # Análisis exploratorio en Jupyter
- app.py # Aplicación principal con Streamlit
- requirements.txt # Dependencias del proyecto
- README.md # Este archivo

## Cómo ejecutar la aplicación

1. Asegúrate de tener creado y activado tu entorno virtual:
```bash
python -m venv vehicles_env
source vehicles_env/bin/activate 
```

2. Instala las dependencias
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

