# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

# to create necessary tkinter widgets
def Widgets():
	link_label = Label(root,
					text="YouTube link :",
					bg="#00FF00")
	link_label.grid(row=1,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=55,
						textvariable=video_Link)
	root.linkText.grid(row=1,
					column=1,
					pady=5,
					padx=5,
					columnspan = 2)

	destination_label = Label(root,
							text="Destination :",
							bg="#00FF00")
	destination_label.grid(row=2,
						column=0,
						pady=5,
						padx=5)

	root.destinationText = Entry(root,
								width=40,
								textvariable=Path)
	root.destinationText.grid(row=2,
							column=1,
							pady=5,
							padx=5)

	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="#05E8E0")
	browse_B.grid(row=2,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download",
						command=Download,
						width=20,
						bg="#05E8E0")
	Download_B.grid(row=3,
					column=1,
					pady=3,
					padx=3)


# destination folder to save the video
def Browse():
	# Presenting user with a pop-up for
	# directory selection. initialdir
	download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

	# Displaying the directory in the directory
	Path.set(download_Directory)

# Defining Download() to download the video
def Download():
	
	# getting user-input Youtube Link
	link = Link.get()
	
	# select the optimal location for saves's file
	download_Folder = Path.get()

	# Creating object of YouTube()
	getVideo = YouTube(link)

	# Getting all the available streams of the
	# youtube video and selecting the first 
	videoStream = getVideo.streams.first()

	# Downloading the video to destination
	videoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
root.geometry("600x120")
root.title("YouTube_Video_Downloader")
root.config(background="#000000")

# Creating the tkinter Variables
Link = StringVar()
Path = StringVar()

# Calling the Widgets() function
Widgets()

# application
root.mainloop()
