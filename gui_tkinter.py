from tkinter import *
import time

executing = True

def create_led(color, position_x, position_y):
    led_canvas = Canvas(app, width=50, height=50, background='#282a36', highlightthickness=0,borderwidth=0)
    led_canvas.create_oval(0, 0, 50, 50, fill=color)
    led_canvas.place(x=position_x,y=position_y)

def loop():
    global executing
    i=0
    pisca = True
    while executing:
        text_command.delete('1.0', END)
        text_command.insert("1.0", str(i))
        if pisca:
            sensor_status.set("Ligado")
            label_status_sensor.place(x=x_sensor0-10,y=y_sensor0+60)
            create_led("lime",x_sensor0, y_sensor0)
            
            rele_status.set("DesLigado")
            label_status_rele.place(x=x_rele0-30,y=y_rele0+60)
            create_led("red",x_rele0, y_rele0)
        else:
            sensor_status.set("Desligado")
            label_status_sensor.place(x=x_sensor0-30,y=y_sensor0+60)
            create_led("red",x_sensor0, y_sensor0)

            rele_status.set("Ligado")
            label_status_rele.place(x=x_rele0-10,y=y_rele0+60)
            create_led("lime",x_rele0, y_rele0)
        time.sleep(1)
        pisca = not pisca
        i = i+1
        app.update()

app = Tk()
x_sensor0 = 100
x_sensor1 = x_sensor0 + 50
y_sensor0 = 73
y_sensor1 = y_sensor0 + 50
x_rele0 = 250
x_rele1 = x_rele0 + 50
y_rele0 = 73
y_rele1 = y_rele0 + 50

app.geometry('400x400')

app.title('Contador de peças')
app.configure(bg='#282a36')

sensor_status = StringVar()

label_sensor = Label(app, text="Sensor", font=("Arial", 15, "bold"),foreground='#f8f8f2', background='#282a36')
label_sensor.place(x=x_sensor0-10,y=y_sensor0-40)
label_status_sensor = Label(app, textvariable=sensor_status, font=("Arial", 15, "bold"),foreground='#f8f8f2', background='#282a36')

rele_status = StringVar()

label_rele = Label(app, text="Rele", font=("Arial", 15, "bold"),foreground='#f8f8f2', background='#282a36')
label_rele.place(x=x_rele0,y=y_rele0-40)
label_status_rele=Label(app, textvariable=rele_status,font=("Arial", 15, "bold"),foreground='#f8f8f2', background='#282a36')

label_execute = Label(app, text="Executando Comando :",font=("Arial", 13, "bold"),background="#282a36",fg="white")
label_execute.place(x=30,y=200)

text_command = Text(app,background="#44475a",fg="white", highlightthickness=0,borderwidth=0,padx=10,pady=5)
text_command.place(x=30,y=230, height=80, width=340)
text_command.insert(END, "")

Label(app, text="Criado por Alex PS - controleeletronica.com.br",font=("Arial", 11, "bold"),background="#282a36",fg="white").pack(side=BOTTOM, padx=20, pady=25)
app.after(200,loop)

app.mainloop()

def terminate():
    global executing
    executing = False
    app.destroy()