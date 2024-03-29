from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import serial
import pygame
from math import ceil

class JoystickController:
    def __init__(self):
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()

        if joystick_count == 0:
            print("No joysticks found.")
            sys.exit(1)

        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

        self.axis = {}
        self.button = [False] * 16
        self.deadzone = {0: 0.15, 1: 0.15, 2: 0.15, 3: 0.15}

        for i in range(6):
            self.axis[i] = 0.0

        for i in range(self.controller.get_numbuttons()):
            self.button[i] = False

    def read_joystick(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

            if event.type == pygame.JOYBUTTONUP:
                self.button[event.button] = False 
              #  print(button)

            if event.type == pygame.JOYBUTTONDOWN:
                self.button[event.button] = True
               # print(button)          

            if event.type == pygame.JOYAXISMOTION:
                self.axis[event.axis] = round(event.value, 3)
               # print(axis)

    def get_data_string(self):
        data = ""
        for i in self.axis:
            data += "#" + str(i) + "@" + str(self.axis[i])
        for i in range(ceil(len(self.button) / 8)):
            data_i = 0
            for j in range(8):
                data_i += 2 ** j * self.button[i * 8 + j]
            data += "#" + str(i + len(self.axis)) + "@" + str(data_i)
        data += "\n"
        return data


class Ui_Form(object):
    def setupUi(self, Form):
        self.data= "0,0"
        Form.setObjectName("Form")
        Form.resize(802, 919)
        self.graph = QtWidgets.QFrame(Form)
        self.graph.setGeometry(QtCore.QRect(30, 10, 751, 481))
        self.graph.setStyleSheet("background-color : rgb(170, 170, 255)")
        self.graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph.setObjectName("graph")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(30, 510, 751, 401))
        self.frame_2.setStyleSheet("background-color: rgb(56, 111, 167)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.x_coord = QtWidgets.QLabel(self.frame_2)
        self.x_coord.setGeometry(QtCore.QRect(140, 40, 141, 41))
        self.x_coord.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.x_coord.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.x_coord.setFont(font)
        self.x_coord.setObjectName("x_coord")
        self.y_coord = QtWidgets.QLabel(self.frame_2)
        self.y_coord.setGeometry(QtCore.QRect(140, 120, 141, 41))
        self.y_coord.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.y_coord.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.y_coord.setFont(font)
        self.y_coord.setObjectName("y_coord")
        self.button0 = QtWidgets.QLabel(self.frame_2)
        self.button0.setGeometry(QtCore.QRect(140, 200, 141, 41))
        self.button0.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.button0.setObjectName("button0")
        self.button1 = QtWidgets.QLabel(self.frame_2)
        self.button1.setGeometry(QtCore.QRect(140, 290, 141, 41))
        self.button1.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QLabel(self.frame_2)
        self.button2.setGeometry(QtCore.QRect(450, 40, 141, 41))
        self.button2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QLabel(self.frame_2)
        self.button3.setGeometry(QtCore.QRect(450, 120, 141, 41))
        self.button3.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.axis0 = QtWidgets.QLabel(self.frame_2)
        self.axis0.setGeometry(QtCore.QRect(450, 200, 141, 41))
        self.axis0.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.axis0.setObjectName("axis0")
        self.axis1 = QtWidgets.QLabel(self.frame_2)
        self.axis1.setGeometry(QtCore.QRect(450, 290, 141, 41))
        self.axis1.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.axis1.setObjectName("axis1")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 55, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color :rgb(255, 170, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(350, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(350, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(350, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(350, 300, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color :rgb(255, 170, 255)")
        self.label_14.setObjectName("label_14")

        #self.ReceivedString = SerialObj.readline().decode('utf-8').rstrip()
        self.coordin = self.data.split(",")
       # self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        graph = QVBoxLayout(self.graph)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        graph.addWidget(self.canvas)
        self.plot_data()

    def plot_data(self):
        plt.clf()
        ax = self.figure.gca()
    
        print(self.coordin)
        var1 = float(self.coordin[0])
        var2 = float(self.coordin[1])
        x = [var1, 2]
        y = [var2, 4]
        ax.set_autoscale_on(False)
        plt.plot(x, y)
        plt.text(var1, var2 , "coordinate")
        plt.text(2,4,"destination")
        ax.axis([0,5,0,5])
        plt.title("Room Coordinates")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        self.x_coord.setText(self.coordin[0])
        self.y_coord.setText(self.coordin[1])
        self.canvas.draw()

if __name__ == "__main__":
    import sys
    import pygame

    pygame.init()

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    SerialObj = serial.Serial('COM5', baudrate=9600, bytesize=8, parity='N', stopbits=1)
    joystick_controller = JoystickController()

    while True:
        joystick_controller.read_joystick()
        data = joystick_controller.get_data_string()
        SerialObj.write(data.encode())

        received_string = SerialObj.readline().decode('utf-8').rstrip()
        coordinates = received_string.split(",")

        ui.coordin = coordinates
        ui.plot_data()

        QtCore.QCoreApplication.processEvents()

    SerialObj.close()
    sys.exit(app.exec_())
