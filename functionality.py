import MAIN_FILE as mfl
import customtkinter as tk
import NOTE_CLASS as nt
from tkinter import messagebox

def Quit(win, GUI):
    win.destroy()
    GUI.deiconify()

def Add_Gui(GUI):
    def ADD(win, GUI):
        try:
            title = Title_Input.get()
            content = Note_Input.get('1.0', tk.END)

            if not title or not content:
                messagebox.showwarning("Warning", "Title and content cannot be empty!")
                return

            d = {'Title': title, 'Contents': content}
            note = nt.Note(d)
            mfl.Write_Note(note)
            messagebox.showinfo("SAVED", "NOTE HAS BEEN SAVED")
            win.destroy()
            GUI.deiconify()
        except Exception as e:
            messagebox.showwarning("Warning", f"ERROR ({e}) OCCURRED")
            return

    GUI.withdraw()

    win = tk.CTk()
    win.resizable(False, False)
    win.geometry('500x500')
    win.title("ADD A NOTE")

    Title = tk.CTkLabel(win, text= "NOTE TITLE" , font=('Helvetica',20))
    Title.pack(pady = 10)

    Title_Input = tk.CTkEntry(win,font=('Helvetica',20))
    Title_Input.pack(pady = 10)

    Note = tk.CTkLabel(win, text= "NOTE CONTENTS" , font=('Helvetica',20))
    Note.pack(pady = 10)

    Note_Input = tk.CTkTextbox(win, font=('Helvetica',20) , height=200,width=400,border_color='#0093E9',border_width=5)
    Note_Input.pack(padx = 10,pady = 10)

    Add_Button = tk.CTkButton(win,text = 'ADD NOTE',font=('Helvetica',10),command = lambda : ADD(win,GUI))
    Add_Button.pack(pady = 10)

    Quit_Button = tk.CTkButton(win, text='QUIT TO MENU', font=('Helvetica', 10), command=lambda: Quit(win, GUI))
    Quit_Button.pack()

    win.mainloop()

def Read_Gui(GUI):
    def Read():
        try:
            title = Title_Output.get()

            if not title:
                tk.messagebox.showwarning("Warning", "Title and content cannot be empty!")
                return

            note = mfl.Read_Note( title )
            if note != None:
                Title_Output.delete(0, tk.END)
                Note_Output.delete('1.0', tk.END)

                Title_Output.insert(tk.END, note['Title'])
                Note_Output.insert(tk.END, note['Contents'])

                Title_Output.configure(state='disabled')
                Note_Output.configure(state='disabled')
            else:
                tk.messagebox.showerror("ERROR","NOTE NOT FOUND")
        except Exception as e:
            tk.messagebox.showwarning("Warning", f"ERROR ({e}) OCCURRED")
            return

    GUI.withdraw()
    win = tk.CTk()
    win.resizable(False, False)
    win.resizable(False, False)
    win.geometry('500x500')
    win.title("READ A NOTE")

    Title = tk.CTkLabel(win, text="NOTE TITLE", font=('Helvetica', 20))
    Title.pack(pady=10)

    Title_Output = tk.CTkEntry(win, font=('Helvetica', 20))
    Title_Output.pack(pady=10)

    Note = tk.CTkLabel(win, text="NOTE CONTENTS", font=('Helvetica', 20))
    Note.pack(pady=10)

    Note_Output = tk.CTkTextbox(win, font=('Helvetica', 20),height=200,width=400,border_color='#0093E9',border_width=5)
    Note_Output.pack(padx=10, pady=10)

    Read_Button = tk.CTkButton(win,text = 'READ',font=('Helvetica',10),command = lambda : Read())
    Read_Button.pack(pady = 10)

    Quit_Button = tk.CTkButton(win, text='QUIT TO MENU', font=('Helvetica', 10), command=lambda: Quit(win, GUI))
    Quit_Button.pack()
    win.mainloop()

def Delete_Gui(GUI):
    def Delete():
        try:
            title = Title_Delete.get()

            if not title:
                messagebox.showwarning("Warning", "Title and content cannot be empty!")
                return
            choice = messagebox.askyesno("DELETE",f"ARE YOU SURE TO DELETE {title} note")
            if choice:
                mfl.Delete_Note( title )
        except Exception as e:
            messagebox.showwarning("Warning", f"ERROR ({e}) OCCURRED")
            return

    GUI.withdraw()

    win = tk.CTk()

    win.geometry('500x500')
    win.title("DELETE A NOTE")

    Title = tk.CTkLabel(win, text="NOTE TITLE", font=('Helvetica', 20))
    Title.pack(pady=10)

    Title_Delete = tk.CTkEntry(win, font=('Helvetica', 20))
    Title_Delete.pack(pady=10)


    Read_Button = tk.CTkButton(win,text = 'DELETE',font=('Helvetica',10),command = lambda : Delete())
    Read_Button.pack(pady = 10)

    Quit_Button = tk.CTkButton(win, text='QUIT TO MENU', font=('Helvetica', 10), command=lambda: Quit(win, GUI))
    Quit_Button.pack()
    win.mainloop()

def Modify_Gui(GUI):
    def Modify():
        try:
            title = Title_Input.get()
            note = Note_Input.get('1.0', tk.END)
            if not title:
                messagebox.showwarning("Warning", "Title and content cannot be empty!")
                return

            note = mfl.Modify_Note( title,note )
        except Exception as e:
            messagebox.showwarning("Warning", f"ERROR ({e}) OCCURRED")
            return

    GUI.withdraw()

    win = tk.CTk()
    win.resizable(False, False)
    win.geometry('500x500')
    win.title("MODIFY A NOTE")

    Title = tk.CTkLabel(win, text="NOTE TITLE", font=('Helvetica', 20))
    Title.pack(pady=10)

    Title_Input = tk.CTkEntry(win, font=('Helvetica', 20))
    Title_Input.pack(pady=10)

    Note = tk.CTkLabel(win, text="NOTE CONTENTS", font=('Helvetica', 20))
    Note.pack(pady=10)

    Note_Input = tk.CTkTextbox(win, font=('Helvetica', 20), height=200,width=400,border_color='#0093E9',border_width=5)
    Note_Input.pack(padx=10, pady=10)

    Read_Button = tk.CTkButton(win,text = 'MODIFY',font=('Helvetica',10),command = lambda : Modify())
    Read_Button.pack(pady = 10)

    Quit_Button = tk.CTkButton(win, text='QUIT TO MENU', font=('Helvetica', 10), command=lambda: Quit(win, GUI) )
    Quit_Button.pack()
    win.mainloop()
