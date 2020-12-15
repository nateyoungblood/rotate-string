string="hello to the world"

def reverse(string):
    li = list(string.split(" ")) 
    li_r=list()
    for x in range(1,len(li)+1):
        li_r.append(li[len(li)-x])
    return li_r 

def listToString(s):  
    str1 = " "  
    return (str1.join(s)) 

print(listToString(reverse(string)))