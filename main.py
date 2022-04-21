import MainPage
import GamePage
import Player as pl


def go_GamePage():
    life = 3
    MainPage.app.exec_()
    GamePage.main()
    player = pl.Player(life, 40, 800)

if __name__ == "__main__":
    MainPage.main()
    MainPage.ui.pushButton.clicked.connect(go_GamePage())


