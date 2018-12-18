from FForm import TForm

class TFNotFound(TForm):
    Title = "Error page "

    def Render(self):
        return self.RenderTpl()
