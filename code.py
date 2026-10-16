from PyQt5.uic import*
from PyQt5.QtWidgets import*
def play():
    a=win.li1.text()
    b=win.li2.text()
    if not int(a)<=0 or not  int(b)<=0 or not 10<=a<=b:
        QMessageBox.critical(win,"erreur","saisir 2 entiers:2<=a<b")
    else:
        ch=lisse(int(a),int(b))
        win.la2.setText(ch)
def lisse(ch):
    ch=""
    for i in range(1,x+1):
        if i% sommediv==0 and racine(n-1):
            n=n+str(i)
        else:
            chercher
    return ch
def chercher():
    n=0
def sommediv(x):
    s=0
    ch=str(x)
    for i in range(1,x+1):
        s=s+str(x)+"/"
        
    return s
def racine(x):
    n=0
    for i in range(n):
        if x<=n==0:
            
            
    
            
            
            
    

app = QApplication([])
win = loadUi ("interface_lisse.ui")
win.show()
win.bt1.clicked.connect (play)
app.exec_()