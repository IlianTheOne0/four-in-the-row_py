import sys

from views.console_view import ConsoleView
from views.tkinter_view import TkinterView

from controllers.console_controller import ConsoleController
from controllers.tkinter_controller import TkinterController

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        view = TkinterView()
        controller = TkinterController(view)
    else:
        view = ConsoleView()
        controller = ConsoleController(view)

    controller.start()

if __name__ == "__main__":
    main()