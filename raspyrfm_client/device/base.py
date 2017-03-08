"""
Base class for all device implementations
"""


class Device:
    def __init__(self, manufacturer: str, model: str):
        self._manufacturer = manufacturer
        self._model = model
        self._channel = None

    def get_manufacturer(self) -> str:
        """
        :return: the device manufacturer
        """
        return self._manufacturer

    def get_model(self) -> str:
        """
        :return: the device model
        """
        return self._model

    def setup_channel(self, **channel_arguments) -> None:
        """
        Sets the channel as multiple arguments.
        See implementation specific details about how the channel should be passed in.

        :param channel_arguments:
        """
        raise NotImplementedError

    def get_channel(self) -> dict:
        """
        :return: the channel setup as a dict
        """
        return self._channel

    def get_supported_actions(self) -> [str]:
        """
        :return: the supported actions of this device
        """
        raise NotImplementedError

    def generate_code(self, action: str) -> str:
        """
        This method should be implemented by inheriting classes

        :param action: action to execute
        :return: signal code
        """
        raise NotImplementedError
