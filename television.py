class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """sets the starting vals"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """turns tv on/off"""
        self.__status = not self.__status

    def mute(self) -> None:
        """mutes and unmutes tv"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Moves channel up"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """moves channel down"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """turns volume up"""
        if self.__status:
            self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """turns volume down"""
        if self.__status:
            self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """shows the tv values"""
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'