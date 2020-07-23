import sys
import os
import pyttsx3
import speech_recognition as sr

__author__ = "sn.lionel90"

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect, QFileInfo
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget,QTextEdit, QLineEdit, QFileDialog,QApplication, QTabWidget,QCheckBox

FONT = QFont ( "Calibri", 20 , weight = 75) #constante de la fuente a nivel de clase 
FONT.setBold(True)

FONT2 = QFont("Calibri", 12, weight = 75)
FONT2.setBold(False)

class Window (QTabWidget): #clase ventana principal
    def __init__(self):  #funcion de inicializacion de la bentana 
        super().__init__() #llamada a superclase
        self.setMaximumSize(440,350) #tamaño maximo
        self.setMinimumSize(440,350) #tamaño minimo
        self.setWindowTitle('TTS, Texto to Speech PyQuendo') #texto de cabecera (titulo)
        self.addTab(TextToVoiceTab(), ' Text to Voice') #pestaña 1
        self.addTab(VoiceToTextTab(), 'Voice To Text')

class TextToVoiceTab(QWidget):
    def __init__(self):
        super().__init__() #llamada de la funcion anterior
        boton_leer = QPushButton('Leer', self) #inicializacion del boton
        boton_leer.setGeometry(QRect(150,260,85,27)) #posicion y tamaño del boton
        boton_leer.clicked.connect(self.callTextovoz) #evento de boton aceptar

        boton_salir = QPushButton('Salir', self) #inicializacion del boton
        boton_salir.setGeometry(QRect(60,260,85,27)) #posicion y tamaño del boton
        boton_salir.clicked.connect(self.salir) #llamando a la funcion de salir

        self.textArea = QTextEdit('  ', self) #inicializacion del area de texto
        self.textArea.setGeometry(QRect(20,70,371,181)) #posicion y tamaño del arera

        labelIntro = QLabel("Escriba el texto para traducir a voz", self)
        labelIntro.setGeometry(QRect(60,10, 301, 80))
        labelIntro.setFont(FONT2)
        labelIntro.setAlignment(Qt.AlignCenter)

        label = QLabel("PyQuendo ©Sn.Lionel90" ,self) #titulo de la pestaña
        label.setGeometry(QRect(60,10, 301,31)) #tamaño y posicion de la pestalña
        label.setFont(FONT) #obtengo la fuente de la variable
        label.setAlignment(Qt.AlignCenter)

    def callTextovoz(self): #llamando a la funcion del evento del boton aceptar
        texto = self.textArea.toPlainText() # a texo plano 
        TextToVoice(texto) #llamada a la funcion de traduccion 
    
    def salir(self):
        exit(0)

class VoiceToTextTab(QWidget):
    def __init__(self):
        super().__init__() #llamada de la funcion anterior

        boton_escucha = QPushButton('Ejecutar Tarea', self)
        boton_escucha.setGeometry(QRect(320,35,85,27))
        boton_escucha.clicked.connect(self.callVoiceTotext)

        self.chekBox = QCheckBox('Utilizar el microfono', self)
        self.chekBox.setGeometry(QRect(10,35,300,20))

        self.textArea = QTextEdit(self)
        self.textArea.setGeometry(QRect(15,60,390,160))
        self.textArea.setReadOnly(True)

        lbl = QLabel("PyQuendo ©Sn.Lionel90", self)
        lbl.setGeometry(QRect(60,10,301,31))
        lbl.setFont(FONT2)
        lbl.setAlignment(Qt.AlignCenter)

    def callVoiceTotext(self):
        useMicro = self.chekBox.isChecked()

        if not useMicro:
            text_box = None

        self.textArea.setPlainText(voiceToText(text_box))

def TextToVoice(texto): #funcion de traduccion
    """"
    parametros: texto -->str
    Texto traduciodo a  voz
    """
    engine = pyttsx3.init() #iniciando el conversor
    engine.setProperty ('ratio' ,100)
    engine.say (texto) #que diga lo que pasemos por texto
    engine.runAndWait()

def voiceToText(self):
    """"
    parametros: pathFile -->str
    returns: audio convertido a string
    """
    MicroEnchufao = True
    ñacañaca = ''
    r = sr.Recognizer()
    if MicroEnchufao:
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                ñacañaca = r.recognize_google(audio)
            except Exception:
                ñacañaca = 'nose entienda na'
    return f'has dicho: \n {ñacañaca}' 

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventana = Window()
    ventana.show()
    app.exec()








