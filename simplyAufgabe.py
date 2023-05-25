#!/usr/bin/env python
# coding: utf-8

# In[51]:


import json
from pprint import pprint

with open("auftrag_onlineshop.json") as json_file:
    auftrag = json.load(json_file) #auftrag ist eine Variablenbezeichnung und kann beliebig verändert
    json_file.close()

#alles unteren Angaben sind Experimente, da ich noch nie mit JSON Dateien gearbeitet habe.    
    
#pprint(auftrag)
#print(auftrag["currency"])

#Überprüfung, ob die Zeile shippingAddress überhaupt exisitert
#Erzeugung der fehlenden Zeilen mit den richtigen Namen
#update: die zwischengespeicherte json Datei wird mit den neuen Begriffen aktualisiert
#die neu erzeugte Zeile wird mit den richtigen Werten aus shippingAddress befüllt (4 mal das gleiche)
#Löschung der nicht mehr erforderlichen Zeilen mit shippingAddress
if "shippingAddress" in auftrag:
    zwischenspeicher = {"CustomerName": " " }
    auftrag.update(zwischenspeicher)
    auftrag["CustomerName"] = auftrag["shippingAddress"]["firstName"] + " " + auftrag["shippingAddress"]["lastName"]
    zwischenspeicher = {"CustomerAddress": " " }
    auftrag.update(zwischenspeicher)
    auftrag["CustomerAddress"] = auftrag["shippingAddress"]["address1"] + " " + auftrag["shippingAddress"]["address2"]
    zwischenspeicher = {"CustomerZipcode": " " }
    auftrag.update(zwischenspeicher)
    auftrag["CustomerZipcode"] = auftrag["shippingAddress"]["zipCode"]
    zwischenspeicher = {"CustomerCity": " " }
    auftrag.update(zwischenspeicher)
    auftrag["CustomerCity"] = auftrag["shippingAddress"]["city"]
    del auftrag["shippingAddress"] 
        
string = auftrag["orderDate"] #Datum als String speichern
#print(string) # test ob es geht
auftrag["orderDate"] = string[0:10] #nur die ersten Zeichen des Datums wieder in orderdate speichern
    
newData = {"pickingDateFrom": "" }
auftrag.update(newData)
auftrag["pickingDateFrom"] = auftrag["orderDate"]

#hier komme ich nicht anf die Listenlänge heran, die natürlich variabel sein soll
#Keine Erfahrung mit Listen und Array in Python, deswegen wird hier die Variable mehrmals überschrieben
for i in range(0,4,1): 
    #print(auftrag["orderItems"][i])
    zwischenspeicher = {"items": [i] }
    auftrag.update(zwischenspeicher)
    auftrag["items"] = auftrag["orderItems"][i]
    
#auftrag.update()
pprint(auftrag)
#print(auftrag)
#file = open('auftrag_onlineshop.json', 'w')
#json.dump(auftrag, file)
#file.close()
#pprint(auftrag)


# In[ ]:





# In[ ]:




