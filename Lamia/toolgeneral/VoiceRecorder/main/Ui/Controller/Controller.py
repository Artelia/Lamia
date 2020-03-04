import logging
from .Mediator import Mediator
from ..Widgets.PlayerWidget import PlayerWidget
from ..Widgets.RecorderWidget import RecorderWidget

class Controller():    

    def __init__(self, parent = None):        
        # super(Controller, self).__init__()

        self._mediator = Mediator.getinstance()
        self._mediator.connect("switch_widget", self.switch_widget)

        self.widgets = {
            # "player" : PlayerWidget()
            "recorder" : RecorderWidget()
        }

    def switch_widget(self, widget_name):
        logging.debug("CONTROLLER: switching to " + widget_name)
        for widget in self.widgets.values():
            widget.hide()         
        self.widgets[widget_name].show()