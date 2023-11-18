from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,QRadioButton, QLabel)
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []

questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина у якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))



app = QApplication([])



btn_OK = QPushButon('Ответить') 
ib_Question = QLabel('Самый сложный вопрос в мире?')


RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
Radiogroup.addButton(rbtn_1)
Radiogroup.addButton(rbtn_2)
Radiogroup.addButton(rbtn_3)
Radiogroup.addButton(rbtn_4)


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


AnsGroupBox = QGroupBox("Результат теста")
ib_Result = QLabel('прав ты или нет?')
ib-Correct = QLabel('ответ будет тут!')



layout_res = QVBoxLayout()
layout_res.addWidget(ib_Result, alignment=(Qt.AlignLeft / Qt.AlignTop)
layout.res.addWidget(ib_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(ib_Question, alignment=(Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


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



def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    '''показать панель ответов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    ib_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    Ib_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct*('правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.total += 1)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.total += 1)
    cur_question = randint(0, len(questions_list) - 1)

    q = questions_list[cur_question]
    ask(q)
    

def click_OK():
    if btn_OK.text() =='Ответить':
        check_answer()
        else:
            next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')


btn_OK.clicked.connect(click_OK)


next_question()
window.resize(400, 300)
window.show()
app.exec()