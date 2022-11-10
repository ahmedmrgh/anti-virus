def askdirectory(self):
    # removes the message from the grid
    self.messageView.grid_forget()

    """Returns a selected directory name."""
    self.dirname = tkFileDialog.askdirectory(**self.dir_opt)
    self.entryVariable.set(self.dirname)
    self.buttonView.configure(state=NORMAL)
    return self.dirname