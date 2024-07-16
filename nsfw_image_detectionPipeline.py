from PIL import Image, ImageFilter
from transformers import pipeline
import os

path_to_images = "images/"  # Directorio de imágenes
output_directory = "censored_images/"  # Directorio para guardar imágenes censuradas

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
