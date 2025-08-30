from dataclasses import dataclass


@dataclass
class ProgramState:
    RUNNING: bool = True
    PAUSED: bool = False
    LOGGED: bool = True
