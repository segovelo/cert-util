README.md
Certutil tool in python

This python script is intended to look for file in downloads and compare against checksums file. Accepts file name as optional parameter, if none is passed latest downloaded  *.exe file will be analysed. Valid sha1/256/512 or md5 file must be in same downlads folder.
Do not forget to change on certutil.py and cert.bat for your local downloads folder path
i.e:

C:\Users\segovelo\cert-util>cert python-3.12.2-amd64.exe
MD5 hash of C:\Users\segovelo\Downloads\python-3.12.2-amd64.exe:       
44abfae489d87cc005d50a9267b5d58d
CertUtil: -hashfile command completed successfully.
python-3.12.2-amd64.exe file is OK :)