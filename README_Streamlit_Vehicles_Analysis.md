# 🚗 Aplicación Streamlit: Análisis de Vehículos Usados

## 📋 Descripción General
Esta aplicación web interactiva permite explorar un conjunto de datos de anuncios de venta de vehículos en **Estados Unidos**, ofreciendo una forma visual e intuitiva de analizar las principales variables que afectan el precio de los autos.

El proyecto combina un análisis exploratorio en **Jupyter Notebook (EDA.ipynb)** con una **interfaz web desarrollada en Streamlit (app.py)** para permitir la exploración dinámica de los datos.

---

## 🧩 Funcionalidad

### 🔹 Visualizaciones Interactivas
- **Histograma dinámico**: muestra la distribución del kilometraje (`odometer`) de los vehículos.  
- **Gráfico de dispersión**: permite analizar la relación entre el **año del modelo (`model_year`)** y el **precio (`price`)**.  

### 🔹 Controles dinámicos
- Filtros interactivos y botones para seleccionar variables.  
- Visualizaciones con **Plotly** para una experiencia fluida y responsiva.  

---

## 📚 Dataset
Archivo: `vehicles_us.csv`  
El dataset contiene información sobre anuncios de vehículos usados, con las siguientes columnas relevantes:

| Columna | Descripción |
|:--|:--|
| `price` | Precio del vehículo en USD |
| `model_year` | Año del modelo |
| `odometer` | Kilometraje total recorrido |
| `fuel` | Tipo de combustible |
| `transmission` | Tipo de transmisión |
| `model` | Modelo del vehículo |
| `type` | Tipo de carrocería |
| `condition` | Estado general del vehículo |

El conjunto de datos fue procesado en el archivo `EDA.ipynb`, donde se limpiaron los valores nulos, se ajustaron tipos de datos y se generaron variables derivadas para la visualización.

---

## 🧠 Estructura del Proyecto
```
Proyecto_Sprint_7/
│
├── vehicles_us.csv             # Dataset principal
├── notebooks/
│   └── EDA.ipynb               # Análisis exploratorio en Jupyter
├── app.py                      # Aplicación principal en Streamlit
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

---

## ⚙️ Tecnologías Utilizadas
- **Python 3.10+**
- **Streamlit** – para la interfaz web interactiva  
- **Plotly** – para la visualización dinámica de datos  
- **Pandas / NumPy** – para manipulación y análisis de datos  
- **Statsmodels** – para cálculos estadísticos  

Dependencias definidas en `requirements.txt`:
```
pandas
streamlit
plotly
statsmodels
```

---

## 🚀 Cómo Ejecutar la Aplicación

### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/aesquivel91/vehicles-analysis-app.git
cd vehicles-analysis-app
```

### 2️⃣ Crea y activa un entorno virtual
```bash
python -m venv vehicles_env
source vehicles_env/bin/activate    # En macOS/Linux
vehicles_env\Scripts\activate     # En Windows
```

### 3️⃣ Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecuta la aplicación
```bash
streamlit run app.py
```

Después de unos segundos, la aplicación estará disponible en tu navegador (por defecto en `http://localhost:8501`).

---

## 🧪 Análisis Exploratorio (EDA)
El análisis previo realizado en el notebook `EDA.ipynb` incluye:
- Inspección inicial de los datos (`.info()`, `.describe()`).  
- Limpieza y conversión de tipos de datos (`model_year`, `odometer`, `price`).  
- Análisis de distribución de precios y kilometraje.  
- Exploración de relaciones entre **precio**, **año del modelo** y **tipo de combustible**.  
- Exportación del dataset limpio para uso en la app.

---

## 💡 Posibles Extensiones
- Incorporar filtros por tipo de combustible o transmisión.  
- Añadir análisis de correlación entre variables.  
- Implementar predicciones de precios con modelos de regresión o machine learning.  
- Desplegar la app en **Streamlit Cloud** o **Render** para acceso público.

---

## 👤 Autor
**Andrés Esquivel Díaz**  
📍 *Data Analyst | Python · SQL · Tableau · Power BI*  
🔗 [LinkedIn](https://www.linkedin.com/in/andres-esquivel-diaz-08691337) · [GitHub](https://github.com/aesquivel91)
