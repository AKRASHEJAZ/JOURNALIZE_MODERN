import NOTE_CLASS as nt
from tkinter import messagebox
import json

d = {"Title": "note 1", "Contents": "i want it working fine and neatly"}
n1 = nt.Note(d)

def Write_Note(Note_Obj):
    '''THS FUNCTION WRITES NOTE TO NOTE.JSON FILE IT HAS IN BUILD EXCEPTION HANDLING'''
    try:
        note = Note_Obj.To_Dict()
        try:
            with open("NOTE.json","r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
                if note not in data:
                    data.append(note)
                else:
                    id = messagebox.showerror("WRITING ERROR",f"NOTE ({note['Title']}) ALREADY EXISTS")
        except (FileNotFoundError , json.JSONDecodeError):
            #EXCEPTION HANDLING IF FILE DOESNOT EXISTS OR IS CORRUPTED
            data = []

        with open("NOTE.json", "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        #OTHER ERRORS
        messagebox.showerror("ERROR",f"THERE OCCURED AN ERROR ({e})")
        data = []

def Read_Note( title ):
    '''THS FUNCTION READS NOTE FROM NOTE.JSON FILE IT HAS IN BUILD EXCEPTION HANDLING'''
    try:

        try:
            #TRYING TO READ FILE
            with open("NOTE.json", "r") as f:
                notes = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            # EXCEPTION HANDLING IF FILE DOESNOT EXISTS OR IS CORRUPTED
            notes = []

        for note in notes:
            if note["Title"] == title:
                return note
        messagebox.showerror("ERROR",f"WRONG TITLE ({title}) OR NOTE NOT FOUND ")
        return None

    except Exception as e:
        # OTHER ERRORS
        messagebox.showerror("ERROR", f"THERE OCCURED AN ERROR ({e})")

def Delete_Note( title ):
    '''THIS FUNCTION SIMPLY DELETES NOTE FROM JSON NOTE FILE IT READS ALL
    ENTRIES,SAVE THEM TO LIST AND THEN REMOVES DESIRED DATA MEMBER'''
    try:
        try:
            with open("NOTE.json","r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
                for note in data:
                    if note['Title']==title:
                        data.remove(note)
                        messagebox.showinfo("NOTE DELETION",f"NOTE ({note['Title']}) HAS BEEN DELETED")
                else:
                    messagebox.showerror("NOTE DELETION",f"NOTE ({note['Title']}) NOT FOUND")
        except (FileNotFoundError , json.JSONDecodeError):
            #EXCEPTION HANDLING IF FILE DOESNOT EXISTS OR IS CORRUPTED
            data = []

        with open("NOTE.json", "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        #OTHER ERRORS
        messagebox.showerror("ERROR",f"THERE OCCURED AN ERROR ({e})")
        data = []

def Modify_Note(title,New_Note):
    '''THIS FUNCTION SIMPLY MODIIFY NOTE FROM JSON NOTE FILE IT READS ALL
    ENTRIES,SAVE THEM TO LIST AND THEN MODIFIES DESIRED DATA MEMBER'''
    try:
        try:
            with open("NOTE.json","r") as f:
                data = json.load(f)
            if not isinstance(data, list):
                 data = []
            for note in data:
                if note['Title'] == title:
                    note['Contents'] = New_Note

        except (FileNotFoundError, json.JSONDecodeError):
        # EXCEPTION HANDLING IF FILE DOESNOT EXISTS OR IS CORRUPTED
            data = []

        with open("NOTE.json", "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showerror("NOTE MODIFICATION", f"NOTE ({note['Title']}) HAS BEEN MODIFIED")

    except Exception as e:
        #OTHER ERRORS
        messagebox.showerror("ERROR",f"THERE OCCURED AN ERROR ({e})")
        data = []
