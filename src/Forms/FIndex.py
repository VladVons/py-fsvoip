from FForm import TForm

class TFIndex(TForm):
    Title    = "Main"

    def Render(self):
        self.Info = {}
        self.Info['AppVer']     = '1.2.3'
        return self.RenderTpl()
