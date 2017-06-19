
import UserDict

def dictionnaire(ch): 
 
 try:
     a = UserDict.UserDict(eval(ch))
     return(a)
 except:
     print "Ce n'est pas un dictionnaire"