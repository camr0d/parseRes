import asyncio
from pyrogram import Client

from main_window import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class HomeScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.maxMessageRequest = 10
        
        # Инициализация подключения к telegram
        self.app = Client("my_account")
        
        # Инициализация действий кнопок
        self.ui.pushButton.clicked.connect(self.calculate)
        
    # Подсчет количества просмотров и участников указанного сообщества
    def calculate(self) -> None:
        average_view = 0
        countMembers = 0
        chat_id = self.ui.linkTelegram.text()
        chat_id = chat_id[chat_id.rfind('/') + 1:len(chat_id)]
        count_elements = int(self.ui.le_countMessage.text())
        with self.app:
            countMembers = self.app.get_chat(chat_id).members_count
            for message in self.app.get_chat_history(chat_id, limit=1):
                maxMessage = message.id
            if (count_elements > maxMessage):
                count_elements = maxMessage - 1 
            for x in range(int(count_elements / self.maxMessageRequest)):
                for message in self.app.get_chat_history(chat_id, limit=self.maxMessageRequest, offset=x * self.maxMessageRequest):
                    average_view += message.views
            if (count_elements % self.maxMessageRequest):
                for message in self.app.get_chat_history(chat_id, limit=count_elements % self.maxMessageRequest, offset=int(count_elements / self.maxMessageRequest) * self.maxMessageRequest):
                    average_view += message.views
        average_view = int(average_view / count_elements)
        self.ui.le_aberageView.setText(str(average_view))
        self.ui.le_countUser.setText(str(countMembers))
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = HomeScreen()
    application.show()
    
    sys.exit(app.exec())