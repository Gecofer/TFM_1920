# TFM 

**Repositorio para el TFM del Máster TECI en el curso 2019/2020**

## Objetivo

MLOps y cómo industrializar el uso de Machine Learning: ejemplo práctico para anticipar el malware en sistemas Windows

### Desafíos

En este trabajo se **desarrolla el enfoque actual de MLOps, desde la perspectiva de las empresas en España y su posible introducción al campo académico**. Además, se abordan distintos aspectos metodológicos, se proponen varias alternativas de arquitectura (herramientas y configuración del sistema) para llevar a cabo un MLOps de éxito. En términos generales, MLOps se basa en los principios y las prácticas de DevOps para aumentar la eficacia de los flujos de trabajo en los proyectos de Machine Learning. Asimismo, se presenta MLOps en casos reales de empresas donde el objetivo de negocio es detectar (predecir) la ocurrencia de un evento - como puede ser el fraude de transacciones online o el malware informático, entre otros. Para ello, será necesario mostrar cómo se desarrolla cada una de las etapas del proceso de modelización, incluyendo varias opciones de creación de variables para el modelo y métricas de diagnosis y selección de modelos de clasificación. Además, de introducir MLflow, plataforma que nos permite gestionar todo el ciclo de vida de Machine Learning.

### Datos

El objetivo de este dataset es **predecir la probabilidad de que una máquina Windows se infecte por varias familias de malware, en función de las diferentes propiedades de esa máquina**. Los datos de telemetría que contienen estas propiedades y las infecciones de la máquina se generaron mediante la combinación de informes y amenazas recopilados por la solución de protección de Microsoft, Windows Defender. Los datos con los que vamos a trabajar han sido obtenidos de Kaggle (https://www.kaggle.com/c/microsoft-malware-prediction/data). Para poder realizar su extracción, es necesario aceptar las reglas. Cada fila de este conjunto de datos corresponde a una máquina, identificada de forma exclusiva por un `MachineIdentifier`, donde `HasDetections` indica que se detectó malware en la máquina (0 FALSO, 1 VERDADERO). Usando la información y las etiquetas en `train.csv`, se debe predecir el valor de `HasDetections` una máquina nueva.

La detección de malware es un problema propio de series temporales, pero se complica al introducir nuevas máquinas, conexiones entre máquinas, máquinas con parches, máquinas con programas beta, máquinas con nuevos sistemas operativos, etc. Es importante, destacar que este conjunto de datos no es representativo de las máquinas de los clientes de Microsoft en la naturaleza; ya que está muestreado para incluir una proporción mucho mayor de máquinas de malware.

## Referencias

### Información administrativa sobre TFM

- [Información general TFM](http://blogs.mat.ucm.es/teci/?page_id=151)
- [Información específica TFM](https://blogs.mat.ucm.es/teci/?page_id=1973)
- [Características TFM](http://blogs.mat.ucm.es/teci/wp-content/uploads/sites/9/2016/11/caracteristica-tfm.pdf)
- [Calendario TFM](http://blogs.mat.ucm.es/teci/wp-content/uploads/sites/9/2019/12/calendario-TFM-19-20.pdf)


<!------
### Soluciones
- https://github.com/imor-de/microsoft_malware_prediction_kaggle_2nd
### Desarrollo del TFM
- [Overleaf](https://www.overleaf.com/read/hysrkqscqfgy)
----->
