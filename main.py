import cv2
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
import os
from PIL import Image
import pytesseract
import pandas as pd


class dispensercode(QMainWindow):
    def __init__(self):

        self.name = 'delila'


super(dispensercode, self).__init__()
loadUi('gui1.ui', self)
self.logic = 0
self.capdone = 0
self.count = 1
self.x = 'm'
self.ver = bool
self.Confirm.clicked.connect(self.confirmed)
self.Camon.clicked.connect(self.Camturn)
self.Capture.clicked.connect(self.captureClicked)
self.reset.clicked.connect(self.Reset)


@pyqtSlot()
def confirmed(self):
    name = self.NameInput.toPlainText()


self.new_name = name
self.label2.setText('Patient name is ' + name)
return self.new_name


def Reset(self):
    self.label1.clear()


self.label2.clear()
self.label3.clear()
self.capdone = 0
self.count = 1
cap = cv2.VideoCapture(1)
cap.release()
self.NameInput.clear()


def Camturn(self):
    cap = cv2.VideoCapture(1)


while cap.isOpened():
    ret, frame = cap.read()
if ret:  # ret is if cam is working
    print('here')
self.displayimage(frame, 1)  # frame is the image
cv2.waitKey()
if self.logic == 2:
    cv2.imwrite('%s.png' % self.new_name, frame)  # %s will be substituted by
%(self.value)
self.logic = 0
self.capdone = 1
print('cap done is ', self.capdone)
cap.release()
cv2.destroyAllWindows()
if self.capdone == 1:
    self.loadClicked()
self.ocr()
self.capdone = 0
# -------------------create verification pop up window-----------------------------------#
msg = QMessageBox()
msg.setWindowTitle('please verify whether the ocr is correct')
msg.setText(' Click "Yes" if true "NO" if false or "Open" if there is a small
edit
')
msg.setIcon(QMessageBox.Question)

msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No |
                       QMessageBox.Open)
msg.setInformativeText(self.text)
msg.buttonClicked.connect(self.popup_button)
x = msg.exec_()

print('this is before if is running')
print(self.ver)
while not self.ver:
    print('this while is running')
    if self.count <= 3:
        self.count = self.count + 1
        cap = cv2.VideoCapture(1)

        while (cap.isOpened()):

            ret, frame1 = cap.read()
            if ret == True:  # ret is if cam is working
                self.label1.clear()
                print('here')
                self.displayimage(frame1, 1)  # frame is the image
                cv2.waitKey()

                if (self.logic == 2):
                    cv2.imwrite('%s.png' % self.new_name, frame1)
                    # %s will be substituted by %(self.value)
                    self.logic = 0
                    self.capdone = 1
                    print('cap done is ', self.capdone)
                    # self.textBrowser1.setText('image saved pres cap for
another
image
')
cap.release()
cv2.destroyAllWindows()

if (self.capdone == 1):
    self.loadClicked()
    self.ocr()
    self.capdone = 0
    # -------------------create verification pop up window-----------------------------------#
    msg = QMessageBox()
    msg.setWindowTitle('Please verify whether the ocr is
    correct
    ')
    msg.setText(' Click "Yes" if true "NO" if false or "Open"
                if there is a
    small
    edit
    ')
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.Yes |
                           QMessageBox.No | QMessageBox.Open)
    msg.setInformativeText(self.text)
    msg.buttonClicked.connect(self.popup_button)
    x = msg.exec_()

    else:
    os.startfile('{}.txt'.format(self.new_name))
    # -------------------create done pop up window-----------------------------------#
    msg1 = QMessageBox()
    msg1.setWindowTitle('notify when done')
    msg1.setText(' Click "Yes" if done')
    msg1.setIcon(QMessageBox.Question)
    msg1.setStandardButtons(QMessageBox.Yes)
    msg1.setInformativeText('Is the work done')
    msg1.buttonClicked.connect(self.popup_button1)
    x = msg1.exec_()
break
self.readlist()
msg1 = QMessageBox()
msg1.setWindowTitle("Please collect the pills")
msg1.setText('final_list2')
msg1.setIcon(QMessageBox.Question)
msg1.setStandardButtons(QMessageBox.Yes)
msg1.setInformativeText('Are the pills connected')
msg1.buttonClicked.connect(self.popup_button3)
x = msg1.exec_()
self.logic = 1
else:
print('return not found')


def captureClicked(self):
    self.logic = 2


def displayimage(self, img, window=1):
    qformat = QImage.Format_Indexed8


if len(img.shape) == 3:
    if (img.shape[2]) == 4:
        qformat = QImage.Format_RGBA8888
else:
    qformat = QImage.Format_RGB888
img = QImage(img, img.shape[1], img.shape[0], qformat)  # Qimage is used to load
the
image
img = img.rgbSwapped()
self.label1.setPixmap(QPixmap.fromImage(img))  # QPixmap is used to show the
image
self.label1.setScaledContents(True)  # scale the image according th the frame
self.label1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


def loadClicked(self):
    img1 = cv2.imread("{}.png".format(self.new_name))


self.displayimagef(img1, 1)
cv2.destroyAllWindows()


def displayimagef(self, img1, window=1):
    qformat = QImage.Format_Indexed8


if len(img1.shape) == 3:
    if (img1.shape[2]) == 4:
        qformat = QImage.Format_RGBA8888
else:
    qformat = QImage.Format_RGB888
img1 = QImage(img1, img1.shape[1], img1.shape[0], qformat)  # Qimage is used
to
load
the
image
img1 = img1.rgbSwapped()
self.label1.setPixmap(QPixmap.fromImage(img1))  # QPixmap is used to show the
image
self.label1.setScaledContents(True)  # scale the image according th the frame
self.label1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


def ocr(self):
    config = ('-l eng --oem 1 --psm 3')


# load the example image and convert it to grayscale
image = cv2.imread("{}.png".format(self.new_name))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
self.text = pytesseract.image_to_string(Image.open(filename), config=config)
os.remove(filename)
self.label3.setText(self.text)
print('converted to text')
# export to .txt file
# stdoutOrigin = sys.stdout
with open("{}.txt".format(self.new_name), "w") as f:
    f.write(self.text)


def popup_button(self, i):
    print(i.text())


if i.text() == '&Yes':
    self.ver = True
print(self.ver)
return self.ver
elif i.text() == '&No':
self.ver = False
print(self.ver)
return self.ver
else:
os.startfile('{}.txt'.format(self.new_name))
# -------------------create done pop up window-----------------------------------#
msg1 = QMessageBox()
msg1.setWindowTitle('notify when done')
msg1.setText(' Click "Yes" if done')
msg1.setIcon(QMessageBox.Question)
msg1.setStandardButtons(QMessageBox.Yes)
msg1.setInformativeText('Is the work done')
msg1.buttonClicked.connect(self.popup_button2)
x = msg1.exec_()


def popup_button1(self, j):
    if j.text() == '&Yes':
        print('yes')

else:
print('no')


def popup_button2(self, j):
    if j.text() == '&Yes':
        self.ver = True


print('yes')
return self.ver
else:
print('no')


def readlist(self):
    with open("{}.txt".format(self.new_name)) as f1:
        os.startfile('{}.txt'.format(self.new_name))


flat_list = [word for line in f1 for word in line.split()]
print(flat_list)
# ---------read the csv file of pills-------------------------------------------#
df = pd.read_excel('items.xlsx', sheet_name=0)  # can also index sheet by name or
fetch
all
sheets
bin_no = df['BIN no'].tolist()
Name = df['Name'].tolist()
content = df['content'].tolist()
print(bin_no)
print(Name)
print(content)
# iterating through the list
final_list = []

final_list1 = []
final_list2 = []
i = 0
for i in range(len(flat_list)):
    print('i', i)
    for j in range(len(Name)):
        print('j', j)
        if Name[j] == flat_list[i]:
            print('found one')
            if content[j] == flat_list[i + 1]:
                print('content correct')
                final_list.append(bin_no[j])
                final_list1.append(bin_no[j])
                final_list.append(Name[j])
                final_list.append(content[j])
                print('list1 appended')
                x = i + 1
                for k in range(x, len(flat_list)):
                    if ('Disp:' or 'Disp' == flat_list[k]):
                        print('flat_list', flat_list[k + 2])
                        final_list.append(flat_list[k + 2])
                        final_list2.append(flat_list[k + 2])
                        break

                    else:
                        continue
else:
    continue
else:
continue
print('final list is ', final_list)
print('final list1 is bin is  ', final_list1)
print('final list2 is no of pills is ', final_list2)
import pyfirmata
from pyfirmata import util
import time

board = pyfirmata.Arduino('COM9')
a = 0
for a in range(len(final_list1)):
    it = util.Iterator(board)
it.start()
if final_list1[a] == 1:
    laser = board.get_pin('d:4:i')
dc = board.get_pin('d:6:p')
servo = board.get_pin('d:3:s')
led = board.get_pin('d:2:o')
elif final_list1[a] == 2:
# laser = board.get_pin('d:4:i')
# dc = board.get_pin('d:6:p')
# servo = board.get_pin('d:3:s')
# led = board.get_pin('d:2:o')
pass
else:
laser = board.get_pin('d:7:i')
dc = board.get_pin('d:11:p')
servo = board.get_pin('d:8:s')
led = board.get_pin('d:5:o')
b = int(final_list2[a])
print(b)
br = 1
print(b)
pill_count = 0
servo.write(50)

time.sleep(1)
servo.write(0)
time.sleep(2)

print('abd')
while True:
    dc.write(0.8)
    print('motor')
    while not laser.read():
        if trig_val == 0:
            pill_count = pill_count + 1
            trig_val = 1
            print(pill_count)

        if pill_count == 4 or pill_count == 8:
            dc.write(0)
            servo.write(30)
            time.sleep(1)
            servo.write(0)
            time.sleep(2)

        if pill_count == b:
            dc.write(0)
            led.write(1)
            time.sleep(2)
            led.write(0)

            br = 0
            break

    while laser.read():
        trig_val = 0

        if pill_count == b:
            break

    if br == 0:
        br = 1
        break

app = QApplication(sys.argv)
window = dispensercode()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')