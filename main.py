import wx
import thread
import os



if __name__ == "__main__":
  app = wx.App()
  
  frame = wx.Frame(None, -1, 'win.py')
  frame.SetSize(0,0,200,50)
  
  openfolderDialog = wx.DirDialog(None, "Choose input directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
  
  openfolderDialog.ShowModal()
  imgFilesPath = openfolderDialog.GetPath()
  print(imgFilesPath)
  openfolderDialog.Destroy()
  if imgFilesPath:
    for file in os.listdir(imgFilesPath):
      if file.endswith(".jpg"):
        imgPath = os.path.join(imgFilesPath, file)
        print(imgPath)
  
  thread.test()