import sys
import os
import pyttsx3
import speech_recognition as sr
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget,QTextEdit, QLineEdit, QFileDialog,QApplication, QTabWidget,QCheckBox

FONT = QFont ( "Calibri", 20 , weight = 75) #constante de la fuente a nivel de clase 
FONT.setBold(True)

class Window (QTabWidget): #clase ventana principal
    def __init__(self):  #funcion de inicializacion de la bentana 
        super().__init__() #llamada a superclase
        self.setMaximumSize(440,350) #tamaño maximo
        self.setMinimumSize(440,350) #tamaño minimo
        self.setWindowTitle('TTS, Texto to Speech PyQuendo') #texto de cabecera (titulo)
        self.addTab(TextTab(), ' Texto') #pestaña 1
        #self.addTab(VoiceTab(), ' Voz')
        

class TextTab(QWidget):
    def __init__(self):
        super().__init__() #llamada de la funcion anterior
        boton_aceptar = QPushButton('aceptar', self) #inicializacion del boton
        boton_aceptar.setGeometry(QRect(310,260,85,27)) #posicion y tamaño del boton
        boton_aceptar.clicked.connect(self.callTextovoz) #evento de boton aceptar

        self.textArea = QTextEdit('Escribe el texto aqui ', self) #inicializacion del area de texto
        self.textArea.setGeometry(QRect(20,70,371,181)) #posicion y tamaño del arera

        label = QLabel("Texto a Voz" ,self) #titulo de la pestaña
        label.setGeometry(QRect(60,10, 301,31)) #tamaño y posicion de la pestalña
        label.setFont(FONT) #obtengo la fuente de la variable
        label.setAlignment(Qt.AlignCenter)

    def callTextovoz(self): #llamando a la funcion del evento del boton aceptar
        texto = self.textArea.toPlainText() # a texo plano 
        funcionTextToVoice(texto) #llamada a la funcion de traduccion 

def funcionTextToVoice(texto):
    """"
    parametros: texto -->str
    Texto traduciodo a  voz
    """
    engine = pyttsx3.init() #iniciando el conversor
    engine.setProperty ('ratio' ,100)
    engine.say (texto) #que diga lo que pasemos por texto
    engine.runAndWait()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventana = Window()
    ventana.show()
    app.exec()








