# Malware Detection

**Repositorio para el TFM del Máster TECI en el curso 2019/2020**

## Antecedentes
Concurso de Kaggle: https://www.kaggle.com/c/microsoft-malware-prediction

## Goal
Anticipar el ataque de virus en sistemas W.indows

## Desafíos

En este trabajo se **desarrolla el enfoque actual de MLOps, desde la perspectiva de las empresas en España**. Además, se abordan aspectos metodológicos, se proponen varias alternativas de arquitectura (herramientas y configuración del sistema) para llevar a cabo un MLOps de éxito. Igualmente, se presenta MLOps utilizado en casos reales de empresas donde el objetivo de negocio es detectar la ocurrencia de un evento - como puede ser el fraude de transacciones online o el malware informático, entre otros. Para ello, será necesario mostrar cómo se desarrolla cada una de las etapas del proceso de modelización, incluyendo varias opciones de creación de variables para el modelo y métricas de diagnosis y selección de modelos de clasificación.

## Datos

[Microsoft Malware Prediction](https://www.kaggle.com/c/microsoft-malware-prediction/data). El objetivo es predecir la probabilidad de que una máquina Windows se infecte por varias familias de malware, en función de las diferentes propiedades de esa máquina. Los datos de telemetría que contienen estas propiedades y las infecciones de la máquina se generaron mediante la combinación de informes y amenazas recopilados por la solución de protección de Microsoft, Windows Defender.

Cada fila de este conjunto de datos corresponde a una máquina, identificada de forma exclusiva por un _MachineIdentifier_ y _HasDetections_ indica que se detectó malware en la máquina. Usando la información y las etiquetas en `train.csv`, se debe predecir el valor de _HasDetections_ para cada máquina en `test.csv`.

La metodología de muestreo utilizada para crear este conjunto de datos se diseñó para cumplir con ciertas restricciones comerciales, tanto en lo que respecta a la privacidad del usuario como al período de tiempo durante el cual la máquina estaba funcionando. La detección de malware es un problema inherentemente de series temporales, pero se complica por la introducción de nuevas máquinas, máquinas que se conectan y desconectan, máquinas que reciben parches, máquinas que reciben nuevos sistemas operativos, etc. Si bien el conjunto de datos ha sido dividido aproximadamente por tiempo, las complicaciones y los requisitos de muestreo mencionados anteriormente pueden significar que puede ver un acuerdo imperfecto entre su validación cruzada, puntajes públicos y privados. Además, este conjunto de datos no es representativo de las máquinas de los clientes de Microsoft en la naturaleza; ya está muestreado para incluir una proporción mucho mayor de máquinas de malware.

## Referencias

### Información administrativa sobre TFM

- [Información general TFM](http://blogs.mat.ucm.es/teci/?page_id=151)
- [Información específica TFM](https://blogs.mat.ucm.es/teci/?page_id=1973)
- [Características TFM](http://blogs.mat.ucm.es/teci/wp-content/uploads/sites/9/2016/11/caracteristica-tfm.pdf)
- [Calendario TFM](http://blogs.mat.ucm.es/teci/wp-content/uploads/sites/9/2019/12/calendario-TFM-19-20.pdf)

### Desarrollo del TFM

- [Overleaf](https://www.overleaf.com/read/rgxgsvwfsnms)


<!------
### Soluciones
- https://github.com/imor-de/microsoft_malware_prediction_kaggle_2nd
----->
