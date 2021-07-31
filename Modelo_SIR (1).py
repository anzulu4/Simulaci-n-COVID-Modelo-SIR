'''                        UNIVERSIDAD DE CUENCA                         '''
'''Integrantes: 
                Bueno Villavicencio Juan Diego
                Heredia León Luis Miguel
                Mejia Reinoso Wilson Fernando
                Zuñiga Luzuriaga Andrea Catalina
    '''

'Librerias necesarias'

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

'Datos del problema'

'Población inicial, N.'
N_pob = 17300
#N_pob=int(input('Total de la población= '))
'Numero Inicial de infectados'
#i_0 = int(input('Numero de inicial de infectados= '))/N_pob
i_0 = 10
'Numero inicial de recuperados'
#r_0 = int(input('Numero de inicial de recuperados= '))
r_0=0
'Fracion suseptible de la proyeccion a infectarse'
s_0 = N_pob
'Tasas de contagio y recuperaciónde COVID-19'
#b= 1/ int(input('Personas contagiadas por día ='))
b = 1/2 # contagio
#k = int(input('Personas recuperadas por día='))
k = 1/3 # recuperación
'N es el numero de particiones del intervalo'
#N = int(input('Numero de particiones del intervalo ='))
N = 200

'Desarrollo del modelo SIR'

def modelo_SIR(b,k,S0,I0,R0,N,N_pob):
    """

    Parameters
    ----------
    b : float
        Contagiados por día.
    k : float
        Recuperados por día.
    S0 : int
        Fracción susptible de la proyección a infectarse.
    I0 : int
        Número inicial de infectados.
    R0 : int
        Numero inicial de recuperados.
    N : int
        Número de particiones del intervalo.
    N_pob : int
        Población inicial.

    Returns
    -------
    s : float
        Decuelve el porcentaje de personas suscptibles.
    i : float
        Devuelve el porcentaje de infectados.
    r : float
        Devuelve el porcentaje de personas recuperadas.

    """
    s=np.zeros(N)                        # Matriz llena de zeros para s, con un total de N ceros.  
    r=np.zeros(N)                        # Matriz llena de zeros para r, con un total de N ceros.
    i=np.zeros(N)                        # Matriz llena de zeros para i, con un total de N ceros.
    'Variables dependientes representan las fracciones de la población total en cada una de las tres categorías'
    s_0=S0/N_pob                         # Fracción susceptible de la población           
    r_0=R0/N_pob                         # Fracción recuperada de la población  
    i_0=I0/N_pob                         # Fracción infectada de la población
    'Obtención de los valores por ecuaciones diferenciales'                    
    for t in range(0,N):
        dsdt = -b*s_0*i_0                # Ecuación susceptible             
        didt = b*s_0*i_0 - k*i_0         # Ecuación infectada
        drdt  = k*i_0                    # Ecuación recuperada
        s_0=s_0 + dsdt                   # Fraccion suseotible + Incremento poblacion susetible 
        r_0=r_0 + drdt                   #Fraccion recuperada + Incremento poblacion poblacion recuoerada 
        i_0=i_0 + didt                   # Fracion infectada + Incremento poblacion infectada
        'Guardar datas en los arreglos de s,i, y r'
        s[t]=s_0
        i[t]=i_0
        r[t]=r_0
    return s, i, r

s,l,r= modelo_SIR(b,k,s_0,i_0,r_0,N,N_pob)

'Grafica del Modelo'

fig=plt.figure()

def modelo_grafica(x):
    """

    Parameters
    ----------
    x : int
        Iterador.

    Returns
    -------
    Esta función devulve cada valor en función del tiempo lo cual se añadirá a la grafica.

    """
    'Gráficas con iteraciones secuenciales'
    plt.plot(s[:x], 'darkorange' ,label='Suscptibles ',linewidth=2)        #Devuelve la grafica de s, iterando con x de forma secuencial 
    plt.plot(r[:x], 'lime', label='Infectados',linewidth=2)                #Devuelve la grafica de r, iterando con x de forma secuencial
    plt.plot(l[:x], 'darkred', label='Recuperados ',linewidth=2)           #Devuelve la grafica de i, iterando con x de forma secuencial
    'Titulo, Nobre de los ejes y leyendas'
    plt.title('Modelo SIR ',weight = 'bold',size = 20)     #Titulo de la grafica 
    plt.xlabel('Tiempo(Días)',size = 15)                                  #Nombre eje x 
    plt.ylabel('Población Total',size = 15)                                 #Nombre eje y 
    plt.legend(['s(t) ','r(t)',' i(t)'],fontsize = 10) #Creación de la leyenda 
    plt.show()

'Animación de la Grafica'
animator=FuncAnimation(fig,modelo_grafica,interval=4)

'Guardado de la animacion'
#animator.save(r'Modelo SIR.gif')