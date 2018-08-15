"""
Created on 9 de ago de 2018

@author: otavio.cruzatto
"""

path_arq_origem = "arquivo_cad.txt"
path_arq_editado = "arquivo_robo.txt"
texto_editado = []

arq_origem = open(path_arq_origem, "r")
texto_original = arq_origem.readlines()
arq_origem.close()

for line in texto_original:
    if "at point" in line:
        x_value = (line[ (line.find("X=") + 2) : (line.find("Y=")) ]).strip()
        y_value = (line[ (line.find("Y=") + 2) : (line.find("Z=")) ]).strip()
        texto_editado.append("MoveL Offs(pInicial, " + x_value + ", " + y_value + ", 0),v1000,fine,tool0;\n")

arq_editado = open(path_arq_editado, "w")
arq_editado.writelines(texto_editado)
arq_editado.close()

print("Finalizado!!!\n\n")