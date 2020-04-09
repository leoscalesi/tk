import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title(" Genios quiz ")
        self.label1=tk.Label(self.ventana1,text=" En que año murio San Martin? ")
        self.label1.grid(column=0,row=0)
        self.seleccion=tk.IntVar()  
        
        self.radio1=tk.Radiobutton(self.ventana1,text=1845,variable=self.seleccion,
                                   value=1)
        self.radio1.grid(column=0,row=1)
        self.radio2=tk.Radiobutton(self.ventana1,text=1848,variable=self.seleccion,
                                   value=2)
        self.radio2.grid(column=0,row=2)
        self.radio3=tk.Radiobutton(self.ventana1,text=1850,variable=self.seleccion,
                                   value=3)
        self.radio3.grid(column=0,row=3)
        self.radio4=tk.Radiobutton(self.ventana1,text=1853,variable=self.seleccion,
                                   value=4)
        self.radio4.grid(column=0,row=4)
        self.boton1=tk.Button(self.ventana1,text=" Verificar respuesta ",
                              command=self.mostrarseleccionado)
        self.boton1.grid(column=0,row=5)
        self.label2=tk.Label(text= " La opcion seleccionada es ")
        self.label2.grid(column=0,row=6)
        
        
        
        self.label1=tk.Label(self.ventana1,text=" En que año murio Manuel Belgrano? ")
        self.label1.grid(column=0,row=7)
        self.seleccion1=tk.IntVar()  
        
        self.radio5=tk.Radiobutton(self.ventana1,text=1820,variable=self.seleccion1,
                                   value=4)
        self.radio5.grid(column=0,row=8)
        self.radio6=tk.Radiobutton(self.ventana1,text=1817,variable=self.seleccion1,
                                   value=5)
        self.radio6.grid(column=0,row=9)
        self.radio7=tk.Radiobutton(self.ventana1,text=1824,variable=self.seleccion1,
                                   value=6)
        self.radio7.grid(column=0,row=10)
        self.radio8=tk.Radiobutton(self.ventana1,text=1827,variable=self.seleccion1,
                                   value=7)
        self.radio8.grid(column=0,row=11)
        self.boton2=tk.Button(self.ventana1,text=" Verificar respuesta ",
                              command=self.mostrarseleccionado1)
        self.boton2.grid(column=0,row=12)
        self.label3=tk.Label(text= " La opcion seleccionada es ")
        self.label3.grid(column=0,row=13)
        
        
        self.label1=tk.Label(self.ventana1,text=" En que año murio Juan Manuel de Rosas? ")
        self.label1.grid(column=0,row=14)
        self.seleccion2=tk.IntVar()
        self.radio9=tk.Radiobutton(self.ventana1,text=1877,variable=self.seleccion2,
                                   value=8)
        self.radio9.grid(column=0,row=15)
        self.radio10=tk.Radiobutton(self.ventana1,text=1880,variable=self.seleccion2,
                                   value=9)
        self.radio10.grid(column=0,row=16)
        self.radio11=tk.Radiobutton(self.ventana1,text=1874,variable=self.seleccion2,
                                   value=10)
        self.radio11.grid(column=0,row=17)
        self.radio12=tk.Radiobutton(self.ventana1,text=1883,variable=self.seleccion2,
                                   value=11)
        self.radio12.grid(column=0,row=18)
        self.boton3=tk.Button(self.ventana1,text=" Verificar respuesta ",
                              command=self.mostrarseleccionado2)
        self.boton3.grid(column=0,row=19)
        self.label4=tk.Label(text= " La opcion seleccionada es ")
        self.label4.grid(column=0,row=20)
        
       
        
        self.ventana1.mainloop()
        
    def mostrarseleccionado(self):
         
         if self.seleccion.get()==1:
             self.label2.configure(text= " Incorrecta ")
         if self.seleccion.get()==2:
             self.label2.configure(text= " Incorrecta ")
         if self.seleccion.get()==3:
             self.label2.configure(text= " Correcta ")
             
         if self.seleccion.get()==4:
             self.label2.configure(text= " Incorrecta ")
         
    
    def mostrarseleccionado1(self):   
         if self.seleccion1.get()==4:
             self.label3.configure(text= " Correcta ")
             
         if self.seleccion1.get()==5:
             self.label3.configure(text= " Incorrecta ")
         if self.seleccion1.get()==6:
             self.label3.configure(text= " Incorrecta ")
         if self.seleccion1.get()==7:
             self.label3.configure(text= " Incorrecta ")
        
    def mostrarseleccionado2(self):   
         if self.seleccion2.get()==8:
             self.label4.configure(text= " Correcta ")
             
         if self.seleccion2.get()==9:
             self.label4.configure(text= " Incorrecta ")
         if self.seleccion2.get()==10:
             self.label4.configure(text= " Incorrecta ")
         if self.seleccion2.get()==11:
             self.label4.configure(text= " Incorrecta ")
        
    
    
    
    

  aplicacion1=Aplicacion()

 # Fin de la aplicacion
