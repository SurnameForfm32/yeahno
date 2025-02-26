Dim fso, txtFile
Set fso = CreateObject("Scripting.FileSystemObject")
Set txtFile = fso.CreateTextFile("C:\Users\Public\thisisunreal.txt", True)
txtFile.WriteLine("yayayaynigggerrrrra")
txtFile.Close
