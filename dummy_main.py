from nicegui import ui

# Note that this is not in a __main__ block.  This is because the code throws a runtime error if ui.run() is called in
#   what it calls a "main guard"
ui.label("This is my first NiceGUI")
ui.run()
