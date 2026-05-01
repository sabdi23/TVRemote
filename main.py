import sys
from PyQt6.QtWidgets import QApplication
from gui import RemoteGUI


def main() -> None:
    """
    Launches the TV Remote application
    """
    app = QApplication(sys.argv)
    window = RemoteGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()