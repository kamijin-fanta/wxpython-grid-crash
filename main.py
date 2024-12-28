import wx
import wx.grid

class MyTable(wx.grid.GridTableBase):
    colLabels = ("Title", "URL")

    data = (("Google", "http://google.com/"),
            ("Yahoo! JAPAN", "http://www.yahoo.co.jp/"),
            ("Python", "http://www.python.org/"),
            ("Python Documentation", "http://docs.python.org/"),
            ("wxPython", "http://www.wxpython.org/"))

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return '#' + str(row + 1)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetNumberRows(self):
        return len(self.data)

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="wxPython Grid Demo", size=(640, 480))
        self.InitializeComponents()

    def InitializeComponents(self):
        grid = wx.grid.Grid(self)
        grid.SetTable(MyTable())
        grid.AutoSize()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
