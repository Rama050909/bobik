from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,QRadioButton, QLabel)


app = QApplication([])


window = QWidget()
window.setWindowTitle('Memo Card')


'''Интерфейс приложения Memory Card'''
btn_OK = QPushButon('Ответить') 
ib_Question = QLabel('в каком году была основана Москва?')


RadioGroupBox = QGroupBox("Варианты ответы")
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans2.addWidget(rbtn_4)


layout_ans1.addLayuot(layout_ans2)
layout_ans1.addLayuot(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(ib_Question, alignment=(Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stertch=2)
layout_line3.addStertch(1)



layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layuot_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


window.setLayout(layout_card)
window.show()
app.exec()
