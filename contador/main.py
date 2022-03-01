import tkinter as tk

root = tk.Tk()
root.geometry("480x360+150+150")
root.title("Bem-vindo ao aplicativo Letter Counter")
message1 = tk.StringVar()
Letter1 = tk.StringVar()


def printt():
    message = message1.get()
    letter = Letter1.get()
    message = message.lower()
    letter = letter.lower()

    # Obtenha a contagem e exiba os resultados.
    letter_count = message.count(letter)
    a = "sua mensagem tem  " + str(letter_count) + " " + letter + " na palavra/mensagem."
    labl = tk.Label(root, text=a, font=("arial", 15), fg="black").place(x=10, y=220)


lbl = tk.Label(root, text="Escreva uma mensagem ou palavra", font=("Ubuntu", 15), fg="black").place(
    x=10, y=10
)
lbl1 = tk.Label(
    root, text="Digite a letra para saber sua quantia ", font=("Ubuntu", 15), fg="black"
).place(x=10, y=80)
E1 = tk.Entry(
    root, font=("arial", 15), textvariable=message1, bg="white", fg="black"
).place(x=10, y=40, height=40, width=340)
E2 = tk.Entry(
    root, font=("arial", 15), textvariable=Letter1, bg="white", fg="black"
).place(x=10, y=120, height=40, width=340)
but = tk.Button(
    root,
    text="Verificar",
    command=printt,
    cursor="hand2",
    font=("Times new roman", 30),
    fg="white",
    bg="black",
).place(x=10, y=170, height=40, width=380)
#print("Neste aplicativo, vou contar o número de vezes que uma letra específica ocorre em uma mensagem.");
# mensagem = input("\nPor favor, digite uma mensagem: ")
# letter = input("Qual letra você gostaria de contar as ocorrências?: ")

root.mainloop()