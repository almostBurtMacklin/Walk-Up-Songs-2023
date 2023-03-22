from cx_Freeze import setup, Executable
  
setup(name = "KCC Walkup Songs" ,
      version = "2023" ,
      description = "" ,
      executables = [Executable("main.py", targetName="WalkUpSongApp.exe", icon = 'favicon.ico',)])