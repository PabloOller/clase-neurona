import streamlit as st
import pandas as pd
import numpy as np


class Neuron:
   def __init__(self, weights = [1,1,1], bias=0, func="relu") -> None:
      self.weights = weights
      self.bias = bias
      self.func = func
   
   def run(self, input_data=[1,1,1]):
      output = 0
      output = float(np.dot(self.weights, input_data)) + self.bias
      if self.func == "relu":
         if output < 0:
            output = 0
      elif self.func == "sigmoide":
         output = 1 / (1 + np.exp(-output))
      elif self.func == "binary":
         if output < 0:
            output = 0
         else:
            output = 1
      return output
   
   def changeBias(self, b=100):
      self.bias=b
   
   def changeWeights(self, new_weights=[1,1,1]):
      self.weights = new_weights
   
   def changeFunction(self, new_func="relu"):
      self.func = new_func


st.image("images/neurona.jpg", width=360)

st.header("Clase neurona")

n1 = Neuron()

arrPesos = [float(n) for n in st.text_input(f"Introduce los valores de los pesos separados por un espacio: ").split()]

n1.changeWeights(arrPesos)

arrEntradas = [float(n) for n in st.text_input(f"Introduce los valores de las entradas separados por un espacio: ").split()]

b = st.number_input("Introduzca el valor del sesgo")

n1.changeBias(b)

func = st.selectbox(
   'Elige la función de activación?',
   ('relu', 'sigmoide', 'binary'))

n1.changeFunction(func)

if st.button("Calcular la salida", "b3"):
   if len(arrEntradas) == len(arrPesos):
      resultado = n1.run(arrEntradas)
      st.text(f"La salida de la neurona es {resultado}")
   else:
      st.text(f"Tiene que haber el mismo valores de entradas y de pesos!")