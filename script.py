# imports
import hashlib
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename


current_dir = os.path.dirname(__file__)

# get files with Virus hashes inside
SHA256_HASHES_pack1 = (current_dir + '\\virus\\SHA256-Hashes_pack1.txt')
SHA256_HASHES_pack2 = (current_dir + '\\virus\\SHA256-Hashes_pack2.txt')
SHA256_HASHES_pack3 = (current_dir + '\\virus\\SHA256-Hashes_pack3.txt')





def openfile():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    file= askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(file)
    return file


def fastscan(file):
    if file ==None:
        pass
    try:

        # default virus found to false
        virus_found = False
        File: {file}

        # open file and get hash
        with open(file, "rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha256(bytes).hexdigest()


        # SHA256 HASHES check + pack 1
        with open(SHA256_HASHES_pack1, 'r') as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                if str(readable_hash) == str(line.split(";")[0]):
                    virus_found = True
                    File: {file}
                    f.close()
        f.close()
        # check if virus is found else pass
        if virus_found == True:
            pass
        else:
            pass
        if virus_found == False:
            # SHA256 HASHES check + pack 2
            with open(SHA256_HASHES_pack2, 'r') as f:
                lines = [line.rstrip() for line in f]
                for line in lines:
                    if str(readable_hash) == str(line.split(";")[0]):
                        virus_found = True
                        f.close()
            f.close()
        else:
            pass
        if virus_found == False:
            # SHA256 HASHES check + pack 3
            with open(SHA256_HASHES_pack3, 'r') as f:
                lines = [line.rstrip() for line in f]
                for line in lines:
                    if str(readable_hash) == str(line.split(";")[0]):
                        virus_found = True
                        f.close()
            f.close()
        else:
            pass
        if virus_found == True:
            delete_file(file)

    except:
        if file and virus_found == False:
            safe()


def delete_file(file):
    try:
        os.remove(file)
    except:
        # file coudn't be deleted = show error message
        cant_msg()
        File: {file}
        not_safe()
    finally:
        removed_msg()
        File: {file}
        safe()


def safe():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text='file is safe')
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def not_safe():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text='file not safe')
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def cant_msg():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text='file cannot be deleted')
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def removed_msg():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text='file is deleted')
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)






chose = Tk()
chose.geometry('400x150')
chose.title('chose')

button1 = Button(chose, text='Chose file',command=lambda: fastscan(openfile()))
button1.place(x=5,y=10)
button1.pack()
chose.mainloop()






