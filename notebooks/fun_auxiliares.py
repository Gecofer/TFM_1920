# Fichero con las funciones auxiliares usadas para los notebooks
# --------------------------------------------------------------

# Importamos las librerías

import pandas as pd
import plotly.figure_factory as ff

import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import scipy.stats as ss

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "none"

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as ss

from plotly import tools
from plotly.offline import init_notebook_mode, iplot

pd.set_option('display.max_columns', 500)


def assess_NA(data):
    '''
    Devuelve un dataframe de pandas que indica el número total de valores 
    de NA y el porcentaje de valores de NA en cada columna.
    
    https://towardsdatascience.com/cleaning-missing-values-in-a-pandas-dataframe-a88b3d1a66bf
    
    Parámetros
    ----------
    data: dataframe
    '''
    
    # pandas series denoting features and the sum of their null values
    null_sum = data.isnull().sum()# instantiate columns for missing data
    total = null_sum.sort_values(ascending=False)
    percent = ( ((null_sum / len(data.index))*100).round(2) ).sort_values(ascending=False)
    
    # concatenate along the columns to create the complete dataframe
    df_NA = pd.concat([total, percent], axis=1, keys=['TotalNA', 'PorcentajeNA'])
    
    # drop rows that don't have any missing data; omit if you want to keep all rows
    df_NA = df_NA[ (df_NA.T != 0).any() ]
    
    return df_NA


def corr(data, variables):
    
    '''
    Devuelve el valor de la correlación entre variables numéricas
    
    Parámetros
    ----------
    data: dataframe
    variables: variable o lista de variables a comparar
    '''
    
    correlacion = data[variables+['HasDetections']].corr()
    correlacion_lista = correlacion.values.tolist()
    correlacion_col = correlacion.columns
    
    return correlacion #, correlacion_lista, correlacion_col


def plot_corr(correlacion):
    
    '''
    Representa de forma gráfica la correlación usando la librería Plotly
    
    
    Parámetros
    ----------
    correlación: salida de la función corr()
    '''
    
    sns_colorscale = [[0.0, '#3f7f93'], #cmap = sns.diverging_palette(220, 10, as_cmap = True)
     [0.071, '#5890a1'],
     [0.143, '#72a1b0'],
     [0.214, '#8cb3bf'],
     [0.286, '#a7c5cf'],
     [0.357, '#c0d6dd'],
     [0.429, '#dae8ec'],
     [0.5, '#f2f2f2'],
     [0.571, '#f7d7d9'],
     [0.643, '#f2bcc0'],
     [0.714, '#eda3a9'],
     [0.786, '#e8888f'],
     [0.857, '#e36e76'],
     [0.929, '#de535e'],
     [1.0, '#d93a46']]
    
    figure = ff.create_annotated_heatmap(
        z=correlacion.values,
        x=list(correlacion.columns),
        y=list(correlacion.index),
        annotation_text=correlacion.round(2).values,
        colorscale=sns_colorscale,
        showscale=True,
    )

    layout_heatmap = go.Layout(
        title=('Matriz de correlación'),
        #xaxis=dict(title='Weekday'), 
        #yaxis=dict(title='Hour', dtick=1),
        yaxis_autorange='reversed',
        title_x=0, 
        width=600, height=600,
        xaxis_showgrid=True,
        yaxis_showgrid=False, margin=dict(l=200, r=0, t=100, b=200),
    )

    fig  = go.FigureWidget(figure)
    fig.layout=layout_heatmap
    fig.layout.annotations = figure.layout.annotations
    #fig.data[0].colorbar = dict(title='Number of visitors', titleside = 'top')
    fig.data[0].colorbar = dict(titleside = 'top')

    iplot(fig)
    
    
def corr_categorical(x, y):
    
    '''
    Devuelve el valor de la correlación entre variables categóricas
    
    Parámetros
    ----------
    x: variable
    y: variable
    '''
    
    confusion_matrix = pd.crosstab(x,y)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    
    return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))


def transform_categorical(cambiar_palabras, variables_categoricas, train, test):

    '''
    Modifica un determinado valor en una columna por otro valor, tanto
    en train como en test
    
    Parámetros
    ----------
    cambiar_palabras: diccionario
    variables_categoricas: variable
    train: dataframe
    test: dataframe
    variables: variable o lista de variables a comparar
    '''
    
    for col in variables_categoricas:
        # Hacemos el cambio en train  
        train.replace({col: cambiar_palabras}, inplace=True)
        # Hacemos el cambio en test  
        test.replace({col: cambiar_palabras}, inplace=True)
    
    return train, test