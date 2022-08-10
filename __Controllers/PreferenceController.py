from __Views.Preference import Preference
from __Models.Settings import Setting

class PreferenceController():
    def __init__(self) -> None:
        super().__init__()

    def bind(self, view:Preference):
        self.view = view
        self.view.create_view()