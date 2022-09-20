Test Script Documentation

---------------------

LOOP 

- For each sub-folder within /Tests do the following: 

1. Clear files from /Tests and copy all the .jack files from the sub-folder to /Test
   (need to save the folder name to run the TestCompare)
2. Run "CompileEngine.py Tests"
3. In the folder: C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\tools\CompareTests
   - Clear files
   - From /Tests/... Copy *.xml to this folder
4. In the folder: C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\tools
   - Run TextComparer.bat on each file:
     " 
     TextComparer.bat 
     C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\tools\CompareTests\main.xml 
     C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\projects\10\CompileEngine\Tests\main.xml
     "

---------------------




---------------------

DETAILED DESCRIPTION

x Go to /Tests and delete all the .jack files

x Go into each folder within /Tests/..., one by one
  eg: Tests/ArrayTest

  
x Copy all the .jack files from that folder into /Tests
  so: Tests/ArrayTest
  contains: Main.jack


x Run CompileEngine on that file
  Executes: "CompileEngine.py Tests"


x Delete all the .xml files in 
  C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\tools\CompareTests


x Copy the *.xml files to:
  C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\tools\CompareTests


x Run TextComparer on each file
  eg  TextComparer.bat 
	C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\tools\CompareTests\main.xml 
      C:\Users\tom\Dropbox\MOOCs\Nand2Tetris\projects\10\CompileEngine\Tests\main.xml




