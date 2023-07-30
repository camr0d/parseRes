import asyncio
from pyrogram import Client
import requests

from main_window import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

# переменные 


class HomeScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.maxMessageRequest = 10
        
        # Инициализация подключения к telegram
        self.app = Client("my_account")
        
        # Инициализация действий кнопок
        self.ui.pushButton.clicked.connect(self.calculateTG)
        self.ui.pushButtonVK.clicked.connect(self.calculateVK)
    
    # Подсчет количества просмотров и участников указанного сообщества в VK
    def calculateVK(self) -> None:
        average_view = 0
        chat_id = self.ui.linkVK.text()
        chat_id = chat_id[chat_id.rfind('/') + 1:len(chat_id)]
        if (self.ui.le_countMessageVK.text() == ""):
            return
        count_elements = int(self.ui.le_countMessageVK.text()) + 1
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={'access_token': TOKEN_USER,
                                        'v': "5.131",
                                        'domain': chat_id,
                                        'count': count_elements,
                                        'filter': str('owner')})
        data = response.json()['response']['items']
        for post in data:
            try:
                if (post["is_pinned"]):
                    count_elements -= 1
                    continue
            except:
                average_view += post["views"]["count"]
        if (count_elements != 0):
            average_view = int(average_view / count_elements)
        response = requests.get('https://api.vk.com/method/groups.getById',
                                params={'access_token': TOKEN_USER,
                                        'v': "5.131",
                                        'group_id': chat_id,
                                        'fields': str('members_count')})
        self.ui.le_aberageViewVK.setText(str(average_view))
        self.ui.le_countUserVK.setText(str(response.json()['response'][0]['members_count']))
    
    # Подсчет количества просмотров и участников указанного сообщества в Telegram
    def calculateTG(self) -> None:
        average_view = 0
        countMembers = 0
        chat_id = self.ui.linkTelegram.text()
        chat_id = chat_id[chat_id.rfind('/') + 1:len(chat_id)]
        if (self.ui.le_countMessage.text() == ""):
            return
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