
class ClickShellException(Exception):
    pass

class CommandChainException(ClickShellException):
    pass

class BashFeatureNotSupported(ClickShellException):
    def __init__(self, feature):
        self.feature = feature
        super().__init__(f"Bash feature \'{feature}\' not supported")
