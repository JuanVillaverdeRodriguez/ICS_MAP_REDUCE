# Práctica ICS: MapReduce con Hadoop

## 📂 Organización

Cada uno de los ejercicios está ubicado en su propia carpeta. Estas carpetas incluyen:
- **`mapper.py`**: Script que implementa la funcionalidad del Mapper.
- **`reducer.py`**: Script que implementa la funcionalidad del Reducer.
- **Archivos de entrada**: Datos necesarios para la ejecución de cada ejercicio.
- **`Makefile`**: Facilita la ejecución de las tareas comunes.

## 🚀 Ejecución

Para ejecutar la práctica, es necesario utilizar un contenedor Docker que contiene Cloudera con Hadoop preinstalado. Desde la terminal de ese contenedor, puedes usar los comandos del `Makefile` para ejecutar las diferentes tareas.

### Comandos disponibles:
- **`make init`**: 
  - Carga los archivos necesarios desde la carpeta local al HDFS (Hadoop Distributed File System).
- **`make run`**: 
  - Ejecuta Hadoop Streaming utilizando `mapper.py` y `reducer.py`, recupera los resultados y los guarda en un archivo llamado `solución.txt`.
- **`make runm`**: 
  - Ejecuta Hadoop Streaming utilizando solo `mapper.py` y recupera los resultados.
- **`make clean`**: 
  - Elimina los resultados del MapReduce tanto del HDFS como de la carpeta local.
- **`make cleanm`**: 
  - Elimina los resultados generados solo por `mapper.py` del HDFS y la carpeta local.

## 👥 Colaboradores

- **Óscar Castillo Fernández**  
- **Eva María Arce Ale**  
- **Juan Villaverde Rodríguez**