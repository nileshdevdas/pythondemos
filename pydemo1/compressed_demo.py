from zipfile import ZipFile

zip = ZipFile("d:/demo1.war", 'r')
zip.printdir()