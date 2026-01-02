F = open("Local.py", "w")
F.write("subject = 100\nprint(subject)")
F.close()
exec (open("Local.py").read())

import os 
print (os.path.isfile("Local.py"))


