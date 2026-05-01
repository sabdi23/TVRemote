from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from television import Television


class RemoteGUI(QMainWindow):
    def __init__(self) -> None:
        """
        Loads the UI and connects all buttons.
        """
        super().__init__()
        uic.loadUi('remote.ui', self)
        self.setFixedSize(self.size())
        self.__tv = Television()
        self.button_power.clicked.connect(self.power)
        self.button_mute.clicked.connect(self.mute)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)
        self.button_volume_up.clicked.connect(self.volume_up)
        self.button_volume_down.clicked.connect(self.volume_down)
        self.update_ui()

    def power(self) -> None:
        """
        Toggles the TV on or off.
        """
        self.__tv.power()
        self.update_ui()

    def mute(self) -> None:
        """
        Toggles mute on or off.
        """
        self.__tv.mute()
        self.update_ui()

    def channel_up(self) -> None:
        """
        Goes to the next channel.
        """
        self.__tv.channel_up()
        self.update_ui()

    def channel_down(self) -> None:
        """
        Goes to the previous channel.
        """
        self.__tv.channel_down()
        self.update_ui()

    def volume_up(self) -> None:
        """
        Increases the volume by one.
        """
        self.__tv.volume_up()
        self.update_ui()

    def volume_down(self) -> None:
        """
        Decreases the volume by one.
        """
        self.__tv.volume_down()
        self.update_ui()

    def update_ui(self) -> None:
        """
        Updates all UI elements to reflect the current TV state.
        """
        status = self.__tv._Television__status
        channel = self.__tv._Television__channel
        volume = self.__tv._Television__volume
        muted = self.__tv._Television__muted

        self.button_mute.setEnabled(status)
        self.button_channel_up.setEnabled(status)
        self.button_channel_down.setEnabled(status)
        self.button_volume_up.setEnabled(status and not muted)
        self.button_volume_down.setEnabled(status and not muted)

        if status:
            self.label_channel.setText(f'Channel: {channel + 1}')
            self.progressBar_volume.setValue(volume)
            self.progressBar_volume.setEnabled(not muted)
            try:
                pixmap = QPixmap(f'Channel{channel + 1}.png')
                self.label_channel_image.setPixmap(pixmap.scaled(
                    self.label_channel_image.width(),
                    self.label_channel_image.height()
                ))
            except Exception:
                self.label_channel_image.clear()
        else:
            self.label_channel.setText('Channel: -')
            self.progressBar_volume.setValue(0)
            self.progressBar_volume.setEnabled(False)
            self.label_channel_image.clear()