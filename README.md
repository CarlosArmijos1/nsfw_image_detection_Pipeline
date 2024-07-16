# nsfw_image_detection_Pipeline

### Descripción del Proyecto

#### NSFW Image Detection and Censorship Pipeline

Este proyecto implementa un pipeline para la clasificación y censura de imágenes NSFW (Not Safe For Work) utilizando el modelo preentrenado de Hugging Face. Las imágenes clasificadas como NSFW son automáticamente desenfocadas y guardadas en un directorio específico, mientras que las imágenes seguras se guardan sin cambios.

#### Estructura del Proyecto

- **images/**: Directorio que contiene las imágenes a ser procesadas.
- **censored_images/**: Directorio donde se guardan las imágenes censuradas o sin cambios.
- **nsfw_image_detectionPipeline.py**: Script principal que realiza la clasificación y censura de imágenes.

#### Requisitos

- `Pillow`: Librería de Python para el procesamiento de imágenes.
- `transformers`: Librería de Hugging Face para el uso de modelos preentrenados.

#### Instalación de Dependencias

Para instalar las dependencias necesarias, puedes usar pip:

```bash
pip install Pillow transformers
```

#### Uso

El script `nsfw_image_detectionPipeline.py` clasifica y censura imágenes en un directorio específico. Sigue los siguientes pasos para ejecutar el script:

1. Coloca las imágenes que deseas procesar en el directorio `images/`.
2. Ejecuta el script:

```bash
python nsfw_image_detectionPipeline.py
```

Las imágenes clasificadas como NSFW serán desenfocadas y guardadas en el directorio `censored_images/`. Las imágenes seguras se guardarán sin cambios en el mismo directorio.
