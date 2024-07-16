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

#### Explicación del Código

```python
from PIL import Image, ImageFilter
from transformers import pipeline
import os

# Directorio de imágenes y de salida
path_to_images = "images/"
output_directory = "censored_images/"

# Asegúrate de que el directorio de salida exista
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def classify_and_censor_images(image_directory, output_directory):
    # Crea el pipeline de clasificación de imágenes usando el modelo preentrenado
    classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
    
    # Itera sobre cada archivo en el directorio
    for filename in os.listdir(image_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Asegúrate de que es una imagen
            image_path = os.path.join(image_directory, filename)
            # Carga la imagen
            img = Image.open(image_path)
            
            # Clasifica la imagen
            results = classifier(img)
            
            # Encuentra el resultado con mayor confianza
            if results:
                highest_confidence_result = max(results, key=lambda x: x['score'])
                label = highest_confidence_result['label']
                confidence = highest_confidence_result['score']
                print(f"Image: {filename} - Label: {label}, Confidence: {confidence:.2f}")
                
                # Si la imagen es clasificada como NSFW, desenfócala y guarda en el directorio de salida
                output_path = os.path.join(output_directory, filename)
                if label == "nsfw":
                    censored_img = img.filter(ImageFilter.GaussianBlur(10))  # Aplica desenfoque
                    censored_img.save(output_path)
                else:
                    # Guarda la imagen sin cambios en el directorio de salida
                    img.save(output_path)

if __name__ == "__main__":
    classify_and_censor_images(path_to_images, output_directory)
```
