from tkinter import *
import socket
from tkinter import filedialog
import Encryption
def send(a):
    for child in st.winfo_children():
        if isinstance(child, Frame):
            child.pack_forget()

    def send_f():
        filename = filedialog.askopenfilename()
        with open(filename, 'rb') as image_file:
          image_binary = image_file.read()
        # Define the server address and port
        image_base64 = Encryption.encode_base64(image_binary)
# Store the Base64-encoded image in a text file
        with open('image_base64.txt', 'w') as text_file:
          text_file.write(image_base64)

        server_host = a  # Replace with the actual server's IP address
        server_port = 12345

        # Open the text file to send
        with open('image_base64.txt', 'rb') as file:
            file_data = file.read()

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_host, server_port))

        # Send the file data to the server
        client_socket.sendall(file_data)

        print("File sent successfully.")

        # Close the client socket
        client_socket.close()
        for child in st.winfo_children():
         if isinstance(child, Frame):
            child.pack_forget()
        ls = Frame(st)
        ls.pack(padx=10, pady=10)
        L1 = Label(ls,text="File sent successfully.")
        L1.pack(side = TOP)

    ls = Frame(st)
    ls.pack(padx=10, pady=10)
    select = Button(ls, text="Select and send files", command=send_f)
    select.pack(side=TOP)

def sel():
    for child in st.winfo_children():
        if isinstance(child, Frame):
            child.pack_forget()
    ls = Frame(st)
    ls.pack(padx=10, pady=10)
    L1 = Label(ls, text="Enter IP Address:")
    L1.pack(side=LEFT)
    E1 = Entry(ls, bd=5)
    E1.pack(side=RIGHT)
    l_s_p = Frame(st)
    l_s_p.pack(padx=10, pady=10)
    select = Button(l_s_p, text="Connect", command=lambda: send(E1.get()))
    select.pack(side=TOP)

st = Tk()
strt = Frame(st)
strt.pack()
login = Button(strt, text="Sender", command=sel)
login.pack(side=TOP)

def run():
    st.mainloop()

if __name__ == "__main__":
    run()