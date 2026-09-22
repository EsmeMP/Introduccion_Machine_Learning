# Base de conocimiento: Machine Learning e IA

Repositorio personal de consulta, refuerzo y comprobación del conocimiento adquirido en distintos cursos de *machine learning*, *deep learning* y agentes de IA. Reúne notebooks, datos, visualizaciones y modelos creados durante las prácticas para conservar ejemplos ejecutables y poder retomar o verificar conceptos concretos.

No pretende ser un curso, una guía curricular ni una introducción autónoma para lectores nuevos. El contenido refleja el avance, las herramientas y los ejercicios de las fuentes de estudio originales; cada notebook puede revisarse de forma independiente según el tema que se quiera reforzar.

## Contenido

| Ruta | Qué se practica |
| --- | --- |
| [`notebooks/Models`](notebooks/Models) | Ejercicios de regresión, linealidad, preparación de datos, K-NN, SVR, árboles, Random Forest, Gradient Boosting y evaluación. |
| [`notebooks/Platzi`](notebooks/Platzi) | Material de apoyo sobre división de conjuntos, escalado, ingeniería y selección de características, regularización, *pipelines*, K-Means, PCA y NLP. |
| [`notebooks/TensorFlow`](notebooks/TensorFlow) | Implementaciones de redes densas, clasificación de imágenes con CNN y *transfer learning*, e *image captioning* con VGG16 y LSTM. |
| [`notebooks/AiAgents`](notebooks/AiAgents) | Ejemplos de construcción de agentes, bucles de ejecución, *tool calling*, framework reutilizable, agente de facturas, patrón MATE y coordinación multiagente. |
| [`datos`](datos) | Conjuntos de datos tabulares usados en las prácticas: vivienda, seguros, comentarios deportivos y datos de partidos/jugadores. |
| [`img`](img) | Figuras de apoyo y pequeñas imágenes empleadas en los ejercicios. |

Los modelos y artefactos generados en las prácticas de TensorFlow se encuentran en [`notebooks/TensorFlow`](notebooks/TensorFlow), por ejemplo `best_model.keras`, archivos `.h5` y `features.dump`.

## Requisitos

- Python 3.13 (el entorno de desarrollo registrado en el proyecto usa 3.13.13).
- `pip` y Jupyter Notebook o JupyterLab.
- Para los notebooks de agentes, una clave de Groq configurada como variable de entorno.

## Instalación

Desde la raíz del repositorio:

```bash
python -m venv .venv
source .venv/bin/activate       # En Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para cubrir dependencias que usan notebooks específicos y que no están fijadas actualmente en `requirements.txt`, instale además:

```bash
python -m pip install groq ipywidgets wordcloud statsmodels
```

Inicie el entorno interactivo:

```bash
jupyter lab
```

Después, abra el notebook que quiera ejecutar desde la interfaz de Jupyter. Como alternativa, puede usar `jupyter notebook`.

## Cómo consultar el material

Los directorios agrupan apuntes y ejercicios por curso o tema, no establecen una secuencia obligatoria. Use los nombres de los notebooks como índice para localizar el concepto que quiera revisar y ejecútelos cuando necesite comprobar una implementación o reproducir un resultado.

En `notebooks/AiAgents`, los notebooks 06–08 reutilizan el framework definido en `4.1_frameworkAgent.ipynb` mediante `%run`; para ejecutar esa serie, conviene abrir primero dicho framework y sus ejercicios anteriores.

## Agentes de IA: configuración

Los ejemplos de `notebooks/AiAgents` utilizan LiteLLM y Groq —principalmente el modelo `groq/openai/gpt-oss-120b`—. Antes de ejecutar esos notebooks, cree un archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=tu_clave_de_groq
```

El archivo `.env` está ignorado por Git. Nunca suba claves al repositorio. Algunos ejercicios también verifican `OPENAI_API_KEY`; configure esa variable solo si va a ejecutar la variante que la requiera.

## Datos y recursos externos

- Los ejercicios tabulares utilizan los archivos incluidos en [`datos`](datos).
- Las prácticas de clasificación de imágenes y *image captioning* esperan conjuntos como Cats vs. Dogs y Flickr8k. Esas carpetas están excluidas del control de versiones por tamaño; deberá descargarlas y ubicarlas en las rutas que indica cada notebook antes de ejecutarlos.
- La descarga de pesos preentrenados de VGG16 puede requerir conexión a Internet en la primera ejecución.

## Conceptos cubiertos

- Aprendizaje supervisado: regresión lineal, K-NN, SVR, árboles de decisión, Random Forest y Gradient Boosting.
- Preparación de datos: partición de datos, escalado Min-Max y estándar, ingeniería y selección de características, regularización y *pipelines*.
- Evaluación: MSE, RMSE, MAE y R².
- Aprendizaje no supervisado: K-Means, interpretación de clústeres y PCA.
- *Deep learning*: redes densas, CNN, *transfer learning* e *image captioning*.
- Sistemas de agentes: memoria, registro y selección de herramientas, llamadas estructuradas a funciones, validación de acciones y coordinación multiagente.

## Estructura

```text
.
├── datos/                  # Datos tabulares de ejemplo
├── img/                    # Imágenes y gráficos de apoyo
├── notebooks/
│   ├── AiAgents/           # Prácticas de agentes y tool calling
│   ├── Models/             # Modelos clásicos de ML
│   ├── Platzi/             # Preparación y análisis de datos
│   └── TensorFlow/         # Deep learning y visión por computadora
├── fundamentos_ML.py       # Apuntes breves sobre tipos de aprendizaje
├── requirements.txt        # Dependencias del entorno
└── notes.txt               # Nota de activación y versión de Python
```

## Alcance

Este repositorio documenta prácticas y comprobaciones personales; no es un paquete de producción ni sustituye el material de los cursos de origen. Revise rutas de archivos, credenciales, costos/cuotas del proveedor de modelos y resultados de cada notebook antes de reutilizar cualquier ejemplo en un caso real.
