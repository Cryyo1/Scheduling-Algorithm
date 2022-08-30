import tkinter as tk
import threading
import time

#fonction de gestion de l'algorithme
canvas=None
index=0
elu_process=None
first_time=True
timer=None
timerQuantum=None
flag=False

#dictionnaire des valeurs d'execution de chaque processus
execution_values={
    "blanc":0, 
    "rouge":0, 
    "vert":0, 
    "bleu":0, 
    "jaune":0
}
#dictionnaire des temps passé en cpu de chaque processus
temps_execution_cpu={
    "blanc":0, 
    "rouge":0, 
    "vert":0, 
    "bleu":0, 
    "jaune":0
   
}
#dictionnaire des priorités de chaque processus
priorite={
    "blanc":9548, 
    "rouge":3121, 
    "vert":1024, 
    "bleu":335, 
    "jaune":110
}
#fonction qui calcule quantum
def quantum(process):
    global priorite    
    temps_de_latence=6
    somme=0
    for prio in priorite.values():
        somme+=prio
    return (priorite[process]*temps_de_latence)/somme
#fonction qui calcule Valeur d'exec    
def executionValue(process):
    global priorite
    global temps_execution_cpu
    
    value=(temps_execution_cpu[process]*1024)/priorite[process]
    return value

#fonction qui démarre l'algorithme
def start_algorithm():
    global timer
    global flag
    global first_time
    first_time=True
    flag=False
    horloge(False)

          
def horloge(quantumCall):
    global timer
    global timerQuantum
    global priorite
    global temps_execution_cpu
    global index
    global elu_process
    global first_time
    global lock
    global execution_values
    global flag
    
    # si c la premiere fois ou la fin de quantum d 'un processus on choisira le prochaine processus elu
    if first_time or quantumCall:
        first_time=False
        if index < 1:
            elu_process=list(execution_values.keys())[index]
            #print(list(execution_values.keys())[index])
            index+=1
        else:
            minimum=min(execution_values.values()) 
            elu_process=getProcess(execution_values,minimum)
            
        #on calcule valeur de quantum de processus elu
        quantumValue=quantum(elu_process)
        #on rajoute au temps passé dans cpu pour le processus
        temps_execution_cpu[elu_process]+=quantumValue
        #une mise a jour des couleurs des cercle
        updateCercle(elu_process)
        #on change les labels de quantum 
        updateQuantum(elu_process,quantumValue)
        timerQuantum = threading.Timer(quantumValue,horloge,args=(True,))
        timerQuantum.start()
    
    #si c l'appelle de horloge de chaque seconde
    if quantumCall == False:
        #on met a jour les valuer executions
        for key in priorite.keys():
            execution_values[key]=executionValue(key)
        #on lance le timer pour la prochaine seconde   
        timer = threading.Timer(1,horloge,args=(False,))
        timer.start()
    
    #verifier si on stop l'algorithme ou non
    if flag==True:
        timer.cancel()
        timerQuantum.cancel()


#la fonction qui cherche le processus de valeur min        
def getProcess(execution_values,value):
    for key in execution_values.keys():
        if execution_values[key]==value:
            return key
    return None

#fonction qui stop l'algorithme
def stop_algorithm():
    global flag
    flag=True
    
    
        
            
# Création de l'interface
def create_circle(canvasName,x, y, r,color,**kwargs):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = color,**kwargs)
tk.Canvas.create_circle = create_circle 

def updateCercle(process):
    if process == "blanc":
        # blanc
        create_circle(canvas,75,75,40,"#fff", outline="#ccc", width=1)
        # rouge
        create_circle(canvas,165,75,40,"#909090", outline="#ccc", width=1)
        # vert
        create_circle(canvas,250,75,40,"#909090", outline="#ccc", width=1)
        # bleu
        create_circle(canvas,335,75,40,"#909090", outline="#ccc", width=1)
        # jaune
        create_circle(canvas,420,75,40,"#909090", outline="#ccc", width=1) 
    elif process == "rouge":
        # blanc
        create_circle(canvas,75,75,40,"#909090", outline="#ccc", width=1)
        # rouge
        create_circle(canvas,165,75,40,"#ff0000", outline="#ccc", width=1)
        # vert
        create_circle(canvas,250,75,40,"#909090", outline="#ccc", width=1)
        # bleu
        create_circle(canvas,335,75,40,"#909090", outline="#ccc", width=1)
        # jaune
        create_circle(canvas,420,75,40,"#909090", outline="#ccc", width=1)  
    elif process == "vert":
        # blanc
        create_circle(canvas,75,75,40,"#909090", outline="#ccc", width=1)
        # rouge
        create_circle(canvas,165,75,40,"#909090", outline="#ccc", width=1)
        # vert
        create_circle(canvas,250,75,40,"#00b050", outline="#ccc", width=1)
        # bleu
        create_circle(canvas,335,75,40,"#909090", outline="#ccc", width=1)
        # jaune
        create_circle(canvas,420,75,40,"#909090", outline="#ccc", width=1)  
    elif process == "bleu":
        # blanc
        create_circle(canvas,75,75,40,"#909090", outline="#ccc", width=1)
        # rouge
        create_circle(canvas,165,75,40,"#909090", outline="#ccc", width=1)
        # vert
        create_circle(canvas,250,75,40,"#909090", outline="#ccc", width=1)
        # bleu
        create_circle(canvas,335,75,40,"#1f4e79", outline="#ccc", width=1)
        # jaune
        create_circle(canvas,420,75,40,"#909090", outline="#ccc", width=1)  
    elif process == "jaune": 
        # blanc
        create_circle(canvas,75,75,40,"#909090", outline="#ccc", width=1)
        # rouge
        create_circle(canvas,165,75,40,"#909090", outline="#ccc", width=1)
        # vert
        create_circle(canvas,250,75,40,"#909090", outline="#ccc", width=1)
        # bleu
        create_circle(canvas,335,75,40,"#909090", outline="#ccc", width=1)
        # jaune
        create_circle(canvas,420,75,40,"#ffc000", outline="#ccc", width=1)    

def updateQuantum(process,value):
    if process == "blanc":
        quantum_blanc.configure(text = "Quantum1:\n {:.4f}".format(value))
    elif process == "rouge":
        quantum_rouge.configure(text = "Quantum2:\n {:.4f}".format(value))
    elif process == "vert":
        quantum_vert.configure(text = "Quantum3:\n {:.4f}".format(value)) 
    elif process == "bleu":
        quantum_bleu.configure(text = "Quantum4:\n {:.4f}".format(value)) 
    elif process == "jaune":
        quantum_jaune.configure(text = "Quantum5:\n {:.4f}".format(value))   
    
    
    
    
    
# create the window
window=tk.Tk()
window.title("Algorithme")
width,height=600,450
window.configure(width=width,height=height)
# set minimum window size value
window.minsize(width,height)
 
# set maximum window size value
window.maxsize(width,height)

# canvas of traffic light
canvas = tk.Canvas(window, width=500, height=200, borderwidth=1, highlightthickness=0)
canvas.place(x=50,y=50)


tk.Label(window,text = "Blanc").place(x=110,y=50)
tk.Label(window,text = "Rouge").place(x=200,y=50)
tk.Label(window,text = "Vert").place(x=285,y=50)
tk.Label(window,text = "Bleu").place(x=370,y=50)
tk.Label(window,text = "Jaune").place(x=455,y=50)
# blanc
create_circle(canvas,75,75,40,"#fff", outline="#ccc", width=1)
# rouge
create_circle(canvas,165,75,40,"#ff0000", outline="#ccc", width=1)
# vert
create_circle(canvas,250,75,40,"#00b050", outline="#ccc", width=1)
# bleu
create_circle(canvas,335,75,40,"#1f4e79", outline="#ccc", width=1)
# jaune
create_circle(canvas,420,75,40,"#ffc000", outline="#ccc", width=1)

#panneau d'affichage des quantums
quantum_blanc=tk.Label(window,text = "Quantum1:")
quantum_rouge=tk.Label(window,text = "Quantum2:")
quantum_vert=tk.Label(window,text = "Quantum3:")
quantum_bleu=tk.Label(window,text = "Quantum4:")
quantum_jaune=tk.Label(window,text = "Quantum5:")

quantum_blanc.place(x=90,y=200)
quantum_rouge.place(x=180,y=200)
quantum_vert.place(x=265,y=200)
quantum_bleu.place(x=350,y=200)
quantum_jaune.place(x=435,y=200)

# Démarrer button
start=tk.Button(window,text="Démarrer",command=start_algorithm)
start.configure(width=10,height=1)
start.place(x=450,y=325)


# Arréter time
stop=tk.Button(window,text="Arréter",command=stop_algorithm)
stop.configure(width=10,height=1)
stop.place(x=450,y=375)


window.mainloop()
        

