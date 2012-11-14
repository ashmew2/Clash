# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal,pyqtSlot

import sys
import os
from PyQt4.QtCore import QTimer
from Play import Ui_MainPlay #Question Window
#from ClashClient import Ui_Clash #Connect Window
from Menu import Ui_Menu #Menu for Playing.
from Final import Ui_Final #Menu for Final
#from SubmitDialog import Ui_Dialog
import resources

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import sys
import sqlite3

QuestionDatabase = sqlite3.connect('finalexport.db')
#QuestionDatabase = sqlite3.connect('test.db')
Database_Cursor = QuestionDatabase.cursor()
Number=raw_input("Hello Volunteer, Enter the Number [1-4][40-42] : ")
TableName='TABLE'+Number

QuestionDatabaseInfo = Database_Cursor.execute("SELECT * from "+TableName+";");
QuestionDatabaseInfo = QuestionDatabaseInfo.fetchall()
QList=[]

for i in range(0,25):
    templist=[]
    for j in range(0,6):
        templist.append(QuestionDatabaseInfo[i][j])
    QList.append(templist)
    
#print QuestionDatabaseInfo 
        
#QList = [["Question 1","1","2","3","4","A"],["Question 2","1a","2a","a3","a4","A"],["Question 3","bb1","bb2","bb3","b4","A"],["Question 4","c1","c2","c3","c4","A"],["Quetsion 5","d1","d2","d3d","4d","A"],["Question 6","1","2","3","4","A"],["Question 7","1a","2a","a3","a4","A"],["Question 8","bb1","bb2","bb3","b4","A"],["Question 9","c1","c2","c3","c4","A"],["Quetsion 10","d1","d2","d3d","4d","A"],["Question 11","1","2","3","4","B"],["Question 12","1a","2a","a3","a4","B"],["Question 13","bb1","bb2","bb3","b4","B"],["Question 14","c1","c2","c3","c4","B"],["Quetsion 15","d1","d2","d3d","4d","B"],["Question 16","1","2","3","4","B"],["Question 17","1a","2a","a3","a4","B"],["Question 18","bb1","bb2","bb3","b4","B"],["Question 19","c1","c2","c3","c4","B"],["Quetsion 20","d1","d2","d3d","4d","B"],["Question 21","1","2","3","4","B"],["Question 22","1a","2a","a3","a4","B"],["Question23","bb1","bb2","bb3","b4","B"],["Question 24","c1","c2","c3","c4","B"],["Quetsion 25","d1","d2","d3d","4d","B"]]
#QList=[]

class MainClientWindow(QtGui.QMainWindow):
    
    NumQuestions=25;
    NumQuestionsUnanswered=NumQuestions;
    QuestionsAnswered=[]
    QuestionsUnanswered=[]
    Score=0
    AnswerToBeChecked=''
    NumQuestionsFromServer=NumQuestions
    EnableButtonList=[]

    for x in range(0,25):
        EnableButtonList.append(1)

    # All are enabled at the beginning.
    for i in range(0,NumQuestions):
        QuestionsUnanswered.append(i)
    
    SetValuesSignal=pyqtSignal(Ui_MainPlay,list,int)
    CurrentQuestionNumber=0; #Pointer to UnansweredQuestions (Indexes)
    
    ClashTimerTimeout=1000    
    ClashTimer=QTimer()
    TimeLeft=1800

    @pyqtSlot()
    def ShowFinalSubmitDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter "FINISH" (No Quotes) to Finish Clash Round 1 :')
        if ok:
            if str(text).lower()=="finish":
                self.ShowFinalScore()
        else:
            self.ShowMainMenu()
                 
    @pyqtSlot()
    def ShowFinalScore(self):
        self.FinalScore=Ui_Final(self.Score)
        self.FinalScore.setupUi(self)
        
    @pyqtSlot()
    def ShowMainMenu(self):

        self.MainMenu=Ui_Menu(self.EnableButtonList)
        self.MainMenu.setupUi(self)
        #I was Removed. if wanted.self.MainMenu.SubmitButton.clicked.connect(self.ShowFinalScore)
        
        self.MainMenu.SubmitButton.clicked.connect(self.ShowFinalSubmitDialog)
        self.MainMenu.pushButton25.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton24.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton23.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton22.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton21.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton20.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton19.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton18.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton17.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton16.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton15.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton14.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton13.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton12.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton11.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton10.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton9.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton8.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton7.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton6.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton5.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton4.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton3.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton2.clicked.connect(self.EmitSelectedValueSignal)
        self.MainMenu.pushButton1.clicked.connect(self.EmitSelectedValueSignal)
    
        
    @pyqtSlot()
    def UpdateTimeLeftBar(self):

        if self.ClashTimer.isActive():
            self.TimeLeft-=1

            if self.TimeLeft==0:
                self.ShowFinalScore()
                
            #print "Time Left is : ",self.TimeLeft
            
            try:
                self.PlayUI.TimeLeftBar.setProperty("intValue",self.TimeLeft)
            except (RuntimeError,AttributeError):
                pass
                
    @pyqtSlot()
    def ConnectionProcess(self):
        #print "Inside Connection Process..."
        #self.ConnectUI.ServerIP=self.ConnectUI.ServerIPBox.text()
#        #self.ConnectUI.ServerPort=int(self.ConnectUI.ServerPortBox.text())
#        self.ConnectUI.ServerIP.setText("192.168.13.37")
#        self.ConnectUI.ServerPort.setText("263437")
        self.ConnectUI.ReceiptID=str(self.ConnectUI.CoderIDBox.text())
        #self.ConnectUI.ServerIP='localhost'
        #self.ConnectUI.ServerPort=26000
        #self.ConnectUI.ReceiptID='713'
        
        #print "ServerIP : ",self.ConnectUI.ServerIP
        #print "ServerPort : ",self.ConnectUI.ServerPort
        #print "Coder ID : ",self.ConnectUI.ReceiptID

        #self.ConnectUI.ClientSocket.connect((self.ConnectUI.ServerIP,self.ConnectUI.ServerPort))
        #self.ConnectUI.ClientSocket.send(self.ConnectUI.ReceiptID)
        #print "Waiting..."
        #self.ConnectUI.WelcomeMessage=self.ConnectUI.ClientSocket.recv(self.ConnectUI.WelcomeMessageSize)

        #print "Got : ",self.ConnectUI.WelcomeMessage

        #if self.ConnectUI.WelcomeMessage==self.ConnectUI.ExpectedWelcomeMessage:
        print "Connection Successful."
        self.ConnectUI.ConnectionSuccessfulSignal.emit()

        #else:
        #    print "Call a Volunteer"
        #    raw_input("")
        #    exit()
    

    @pyqtSlot()
    def AcceptQuestions(self):
        #print "Here......>"
        '''
        self.NextSizeSIZE=4

        for i in range(0,self.NumQuestionsFromServer):
            QList.append(["","","","","",""]) #Empty Template
            
            for j in range(0,6):  
            #Six Because there are six fragments, the Question , options and ANSWER
                NextSize=int(self.ConnectUI.ClientSocket.recv(self.NextSizeSIZE))
                QList[i][j]=str(self.ConnectUI.ClientSocket.recv(NextSize))
                
        
        #print QList
        #self.ShowPlayWindow() <=============ShowMenu() Here.
        '''  
        self.ShowMainMenu()
        
    @pyqtSlot()
    def EmitSelectedValueSignal(self):
        SenderName=str(self.sender().objectName())
        #print "Received from : ",SenderName
        #print SenderName," is of type : ",type(SenderName)
        #print "SLICE ===>>>>",SenderName[len("pushButton"):]
        
        QuestionNumber=int(SenderName[len("pushButton"):])-1 #For Index Correction, -1 offset
        #print "Value of QNO : ",QuestionNumber

        #self.CurrentQuestionNumber%=self.NumQuestionsUnanswered
        self.ShowPlayWindow()

        self.CurrentQuestionNumber=self.QuestionsUnanswered.index(QuestionNumber)
        self.SetValuesSignal.emit(self.PlayUI,QList,QuestionNumber)
        

#            self.SetValuesSignal.emit(self.PlayUI,QList,self.QuestionUnanswered[self.CurrentQuestionNumber])

    @pyqtSlot()
    def EmitNextValueSignal(self):
        self.CurrentQuestionNumber+=1
        self.CurrentQuestionNumber%=self.NumQuestionsUnanswered
        self.SetValuesSignal.emit(self.PlayUI,QList,self.QuestionsUnanswered[self.CurrentQuestionNumber])

    @pyqtSlot()
    def UpdateSubmission(self):
        #print "Questions Remaining : ",self.NumQuestionsUnanswered
        #print "Question Index : ",self.CurrentQuestionNumber
        #SCORING TO BE ADDED
        
        self.EnableButtonList[self.QuestionsUnanswered[self.CurrentQuestionNumber]]=0
        print "status(a)",self.PlayUI.Aradio_button.isChecked()
        print "status(b)",self.PlayUI.b_radio_button.isChecked()
        print "status(c)",self.PlayUI.c_radio_button.isChecked()
        print "status(d)",self.PlayUI.d_radio_button.isChecked()
        
        if  self.PlayUI.Aradio_button.isChecked()==1:
            self.AnswerToBeChecked='A'
        
        elif self.PlayUI.b_radio_button.isChecked()==1:
            self.AnswerToBeChecked='B'

        elif self.PlayUI.c_radio_button.isChecked()==1:
            self.AnswerToBeChecked='C'

        elif self.PlayUI.d_radio_button.isChecked()==1:
            self.AnswerToBeChecked='D'

        print "You Answered : ",self.AnswerToBeChecked
        print "Answer Should Be :",QList[self.QuestionsUnanswered[self.CurrentQuestionNumber]][5]

        if self.AnswerToBeChecked==QList[self.QuestionsUnanswered[self.CurrentQuestionNumber]][5]:
            self.Score+=4
        else:
            self.Score-=2
        
        self.PlayUI.ScoreLCD.setProperty("intValue", self.Score)
        
        self.QuestionsAnswered.append(self.QuestionsUnanswered[self.CurrentQuestionNumber])
        self.QuestionsUnanswered.remove(self.QuestionsUnanswered[self.CurrentQuestionNumber])
        
        self.NumQuestionsUnanswered-=1
       
        if self.NumQuestionsUnanswered==0:
            self.ShowFinalScore()
        else:
        #For Changing Question After Submission.
            if self.CurrentQuestionNumber==(self.NumQuestionsUnanswered):
                self.CurrentQuestionNumber=0
            self.SetValuesSignal.emit(self.PlayUI,QList,self.QuestionsUnanswered[self.CurrentQuestionNumber])
        #No need of Index Change

    def EmitPrevValueSignal(self):
        self.CurrentQuestionNumber-=1
        self.CurrentQuestionNumber%=self.NumQuestionsUnanswered
        self.SetValuesSignal.emit(self.PlayUI,QList,self.QuestionsUnanswered[self.CurrentQuestionNumber])

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #self.MainMenu=Ui_Menu()
        #self.MainMenu.setupUi(self)

#        self.ConnectUI=Ui_Clash()
#        self.ConnectUI.setupUi(self)
        #self.PlayUI=Ui_MainPlay()
        #self.PlayUI.setupUi(self)
        #raw_input("ASDASD")
        #exit()
#        self.ConnectUI.ConnectButton.clicked.connect(self.ConnectionProcess)     
#        self.ConnectUI.ConnectionSuccessfulSignal.connect(self.AcceptQuestions)
        self.ClashTimer.timeout.connect(self.UpdateTimeLeftBar)
        self.ClashTimer.setInterval(self.ClashTimerTimeout)
        self.ShowMainMenu()
        #self.ConnectUI.setupUi(self)

        
    def ShowPlayWindow(self):
        self.PlayUI=Ui_MainPlay(self.Score,self.TimeLeft)
        self.PlayUI.setupUi(self)
        #self.PlayUI.ScoreLCD.setProperty("intValue", self.Score)
        #self.PlayUI.TimeLeftBar.setProperty("intValue",self.
        if self.ClashTimer.isActive()==0:
            self.ClashTimer.start()
                                            
        #
        #self.connect(self.ConnectUI, pyqtSignal("ConnectionSuccessfulSignal()"),self, pyqtSlot("AcceptQuestions()"))

#        self.ConnectWindow.
        #
        self.PlayUI.MenuButton.clicked.connect(self.ShowMainMenu)
        self.SetValuesSignal.connect(self.PlayUI.SetValues)
        self.PlayUI.NextQuesButton.clicked.connect(self.EmitNextValueSignal)
        self.SetValuesSignal.emit(self.PlayUI,QList,self.QuestionsUnanswered[self.CurrentQuestionNumber]);#For initial Question

        self.SetValuesSignal.connect(self.PlayUI.SetValues)
        self.PlayUI.PrevQuesButton.clicked.connect(self.EmitPrevValueSignal)
        self.PlayUI.SubmitButton.clicked.connect(self.UpdateSubmission)


def main():
     app = QtGui.QApplication(sys.argv)
     MainWindow = MainClientWindow()

     MainWindow.show()
     sys.exit(app.exec_())


if __name__=="__main__":	
     main()
