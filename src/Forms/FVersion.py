from FForm import TForm

class TFVersion(TForm):
    Title = "Version"

    def Render(self):
        self.Info = {}
        self.Info['AppVer']     = 'Version'
        return self.RenderTpl()
