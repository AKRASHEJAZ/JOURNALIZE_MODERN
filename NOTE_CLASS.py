from tkinter import messagebox


# CLASS NOTE TO PROVIDE PROTOTYPE FOR A NOTE AND INCLUDE ALL POSSIBLE METHODS ANS ATTRIBUTES
class Note:

    def __init__(self, info={}):
        #CONSTRUCTOR FOR NOTE WHICH TAKES NOTE DICTONARY
        #POSSIBLE EXCEPTION FOR EMPTY DICTONARY IS HANDELED

        self.Title = info["Title"]
        self.Contents = info["Contents"]

    def To_Dict(self):
        #METHOD TO CONVERT AND RETURN OBJECT AS DICTONARY FOR STORAGE
        #POSSIBLE EXCEPTION FOR EMPTY DICTONARY IS HANDELED
        Dict_Note = {}
        Dict_Note["Title"] = self.Title
        Dict_Note["Contents"] = self.Contents

        return Dict_Note




