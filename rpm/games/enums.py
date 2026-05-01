from enum import Enum

class GameStatus(str, Enum):
    BACKLOG = "Backlog"
    PLAYING = "Playing"
    COMPLETED = "Completed"
    DROPPED = "Dropped"

class GamePlatform(str, Enum):
    STEAM = "Steam"
    EPIC = "Epic"
    GOG = "GOG"
    OTHER = "Other"
