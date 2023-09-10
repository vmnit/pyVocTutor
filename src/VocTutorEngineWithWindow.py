# import datetime
# import os.path
# import tkinter as tk
# from functools import partial
# from tkinter import filedialog
#
# from VocTutorEngine import VocTutorEngine
#
#
# class VocTutorEngineWithWindow(VocTutorEngine):
#     def __init__(self, root_dir):
#         super.__init__(root_dir)
#         self.mainMenuWin = None
#         self.initiateMainMenuWin()
#
#     def initiateMainMenuWin(self):
#         self.mainMenuWin = tk.Tk()
#         self.mainMenuWin.title(self.title)
#
#         # Users Menu
#         self.createUsersMenu()
#
#         # File Options
#
#     def createUsersMenu(self):
#         user_options = self.get_users()
#         if len(user_options) == 0:
#             self.menuForNewUser()
#         else:
#             self.menuForExistingUser(user_options)
#
#         self.mainMenuWin.mainloop()
#
#     def menuForNewUser(self):
#         self.create_user()
#         self.createBrowseFileMenu()
#
#     def menuForExistingUser(self, user_options):
#         # Create a StringVar to store the selected option
#         selected_user = tk.StringVar()
#
#         # Create Users Menu Widget
#         users_menu = tk.OptionMenu(self.mainMenuWin, selected_user, *user_options)
#         users_menu.pack()
#
#         # selected_vocab_file = tk.StringVar()
#         # file_options = self.get_file_options(selected_user.get())
#         # # Create Users Menu Widget
#         # files_menu = tk.OptionMenu(self.mainMenuWin, selected_vocab_file, *file_options)
#         # files_menu.pack()
#
#     def create_user(self):
#         user_lbl = tk.Label(self.mainMenuWin, text="Enter user name: ")
#         user_lbl.pack()
#
#         user_input = tk.Entry(self.mainMenuWin)
#         user_input.pack()
#
#         btn = tk.Button(self.mainMenuWin, text="Add User", command=partial(self.get_user_value, user_input))
#         btn.pack()
#
#     def createBrowseFileMenu(self):
#         browse_btn = tk.Button(self.mainMenuWin, text="Browse Vocab file", command=self.browse_file)
#         browse_btn.pack()
#
#     def browse_file(self):
#         filetypes = (
#             ('CSV files', '*.csv'),
#             ('All files', '*.*')
#         )
#         file_path = filedialog.askopenfilename(title='Open Vocabulary file', initialdir='C:/', filetypes=filetypes)
#         if file_path:
#             self.selected_vocab_file = file_path
#             lbl = tk.Label(self.mainMenuWin, text=self.selected_vocab_file)
#             lbl.pack()
#
#     def get_user_value(self, user_input):
#         self.selected_user = user_input.get()
#         lbl = tk.Label(self.mainMenuWin, text=self.selected_user)
#         lbl.pack()
#
#
#
# #
# # # first window
# # mainMenuWin = tk.Tk()
# # mainMenuWin.title("PyVocTutor: Best Vocabulary tutor")
# #
# # # option menu
# # options = getVocabFiles(cfg)
# # mainMenu = ttk.OptionMenu(mainMenuWin, 'Data File (CSV)')
# # mainMenu.pack(side=tk.TOP)
# #
# # que = ttk.Label(q_win, text='wordy question')
# # que.pack(side=tk.TOP)
# #
# # create_options()
# #
# # bt = ttk.Button(q_win, text='Submit', command=show_ans)
# # bt.pack(anchor=tk.S)
# #
# #
# # q_win.mainloop()
# # ans = tk.IntVar()
# #
# # CFG_FILE = 'pyVocTutor.cfg'
# #
# # def create_options():
# #     for i in range(1, 7):
# #         rad = ttk.Radiobutton(q_win, text=f'option {i}', value=i, variable=ans)
# #         #rad.pack(anchor=W)
# #         rad.pack(fill='x', padx=5, pady=5)
# #
# # def show_ans():
# #     showinfo(
# #         title='Result',
# #         message=ans.get()
# #     )
#
# # import json
# # import os.path
# # from tkinter import ttk
# # from tkinter.messagebox import showinfo
