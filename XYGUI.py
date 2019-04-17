import wx

def load(event):
    file = open(fileName.GetValue())
    print(file)
    fileContent.setValue(file.read())
    file.close()

def save(event):
    file = open(fileName.GetValue(), 'w')
    file.write(fileContent.GetValue())
    file.close()

#  先创建一个程序
app = wx.App()
# 创建窗口
frm = wx.Frame(None, title = 'Hello world')
# 显示
frm.Show()

openBtn = wx.Button(frm, label='Open', pos=(225, 5), size=(80, 25))
openBtn.Bind(wx.EVT_BUTTON, load)

saveBtn = wx.Button(frm, label='Save', pos=(315, 5), size=(80, 25))
saveBtn.Bind(wx.EVT_BUTTON, save)

fileName = wx.TextCtrl(frm, pos=(5, 5), size=(210, 25))
fileName = wx.TextCtrl(frm, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)

# 运行主程序
app.MainLoop()