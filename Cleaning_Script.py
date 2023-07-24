import os
import re

def clean_text(text, regex_list):
    # Eliminar espacios en blanco al principio y al final del texto
    cleaned_text = text.strip()
    
    # Eliminar expresiones regulares especificadas en la lista regex_list
    for regex_pattern in regex_list:
        cleaned_text = re.sub(regex_pattern, '', cleaned_text)
    
    return cleaned_text

def clone_and_clean_files(folder_path, regex_list):
    # Verificar si la ruta de la carpeta es válida
    if not os.path.exists(folder_path):
        print("La ruta de la carpeta no es válida.")
        return
    
    # Crear una nueva carpeta con el sufijo "_cleaned"
    new_folder_path = folder_path + "_cleaned"
    os.makedirs(new_folder_path, exist_ok=True)
    
    # Obtener la lista de archivos en la carpeta
    file_list = os.listdir(folder_path)
    
    for file_name in file_list:
        # Comprobar si el elemento es un archivo (no un directorio)
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Leer el contenido del archivo
            with open(file_path, 'r', encoding='latin-1') as file:
                text = file.read()
            
            # Limpiar el texto usando la función clean_text
            cleaned_text = clean_text(text, regex_list)
            
            # Crear el nuevo archivo con el sufijo "_cleaned"
            new_file_name = os.path.splitext(file_name)[0] + "_cleaned" + os.path.splitext(file_name)[1]
            new_file_path = os.path.join(new_folder_path, new_file_name)
            
            # Escribir el texto limpio en el nuevo archivo
            with open(new_file_path, 'w', encoding='latin-1') as new_file:
                new_file.write(cleaned_text)

if __name__ == "__main__":
    # Pedir al usuario la ruta de la carpeta y las expresiones regulares
    folder_path = input("Ingrese la ruta de la carpeta: ")
    regex_list = input("Ingrese las expresiones regulares separadas por comas: ").split(',')
    
    # Llamar a la función para clonar y limpiar los archivos
    clone_and_clean_files(folder_path, regex_list)
    print("Proceso completado.")
