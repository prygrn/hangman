import PySimpleGUI as gui

class Hangman:
    def __init__(self) -> None:
        self._window = gui.Window(
            title="Hangman", 
            layout=[[]],
            finalize=True,
            margins=(100, 100)
        )
        
    def readEvent(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        print("Event triggered from user")
        return event_id
    
    def close(self):
        self._window.close
        
        
if __name__ == "__main__":
    game = Hangman()
    # Event loop
    while True:
        event_id = game.readEvent()
        if event_id in {gui.WIN_CLOSED}:
            game.close()