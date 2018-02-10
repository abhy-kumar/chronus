import feedparser       # This library is VVIP. It is used for parsing the RSS feeds. 
import os
import sys
import webbrowser
import errno

# Rest of the libraries are for system compatibilites and usage of internet and all.

try:
    from Tkinter import *  # if the user has python 2 installed.
except:
    from tkinter import *  # if the user has python 3 installed

import appdirs              # for Saving User's preferences and feeds
from tkinter import ttk

appname = "Chronus"
appauthor = "Abhishek Kumar"  # If the data directory doesn't exist, create it
datadir = appdirs.user_data_dir(appname, appauthor)
if (not os.path.isdir(datadir)):
    os.makedirs(datadir)

# Path for saved RSS site feeds for saving.
path = os.path.join(datadir, "sites.txt")

urls = []
buttons = []
text = []

root = Tk()
root.wm_title("Chronus")                    # title of application
root.iconbitmap('iconbeta2.ico')            #icon goes here
addRSSButton = None
refreshRSSButton = None
noMoreEntries = []
websites = []
websiteButtons = []

# ^Above entries are for initializing the respective variables.
root.configure(background='white')          # bg

# all functions starting with def are for specfic functions. THis is is for main GUI
def mainGUI(text):
    global addRSSButton, refreshRSSButton, noMoreEntries
    global websites, buttons, urls
    # Go through each line in sites.txt
    for line in text:
        line = line.strip()
        # we don't want to process the same URL more than once
        if line in urls:
            continue

        urls.append(line)
        # Feed line found in file to feedparser
        site = feedparser.parse(line)
        # Create labels for each site gotten out of the file
        # websites.append(Label(root, text=line))
        # websites[-1].pack()

        num = min(20, len(site['entries']))
        # Top three entries from the RSS feed
        for entry in site['entries'][:num]:
            title = entry['title']

            callback = lambda link=entry['link']: openSite(link)
            buttons.append(ttk.Button(root, text=title, command=callback))

            buttons[-1].pack(padx=30, pady=15)
        noMoreEntries.append(Label(root, text="---End of List---"))
        noMoreEntries[-1].pack(padx=5, pady=5)

    # Make button for adding RSS feeds to the file
    addRSSButton = ttk.Button(root, text="+", command=lambda: addFeedWindow())
    addRSSButton.pack(side="right")
    # Make button for removing RSS feeds from the list
    global removeRSSButton
    removeRSSButton = ttk.Button(root, text="-", command=lambda: removeFeedWindow())
    removeRSSButton.pack(side="right")
    refreshRSSButton = ttk.Button(root, text="↻", command=lambda: refreshRSS())
    refreshRSSButton.pack(side="right")
    cheerbutton = ttk.Button(root, text="Cheer Me Up!", command=lambda: cheerWindows())
    cheerbutton.pack(side="left")
    borebutton = ttk.Button(root, text="I Am Bored", command=lambda: bored())
    borebutton.pack(side="left")

def cheerWindows():                 # This function is for making the user happy by showing happy news
    global cheer
    cheer = Toplevel()
    cheer.wm_title("Cheer Me Up!")

    site = feedparser.parse('https://feeds.feedburner.com/SunnySkyz')
    num = min(7, len(site['entries']))

    for entry in site['entries'][:num]:
        title = entry['title']
        callback = lambda link=entry['link']: openSite(link)
        buttons.append(ttk.Button(cheer, text=title, command=callback))
        buttons[-1].pack(padx=30, pady=15)

def bored():                    # if the user is bored....
    global bore
    bore = Toplevel()
    bore.wm_title("I am bored")

    site = feedparser.parse('http://feeds.reuters.com/reuters/INoddlyEnoughNews')
    num = min(7, len(site['entries']))

    for entry in site['entries'][:num]:
        title = entry['title']
        callback = lambda link=entry['link']: openSite(link)
        buttons.append(ttk.Button(bore, text=title, command=callback))
        buttons[-1].pack(padx=30, pady=15)

def openSite(text):             # Open sites, uses the 'os' library as mentioned above in import statements
    webbrowser.get().open(text)


# Create new window for adding new RSS feed to file.
def addFeedWindow():
    global feed
    feed = Toplevel()
    feed.wm_title("Add new RSS feed")

    newFeedButton = ttk.Button(feed, text="Add New Feed", command=lambda: addFeed())
    newFeedButton.pack(side="right")

    global newFeedGet
    newFeedGet = ttk.Entry(feed, width=50)
    newFeedGet.pack(side="left")


def removeFeed(site):
    for i in range(0, len(urls)):
        if site == urls[i]:
            del urls[i]
        else:
            continue
        with open(path, 'w') as f:
            for i in range(0, len(urls)):
                f.write(urls[i] + "\n")
    remove.destroy()
    refreshRSS()


def removeFeedWindow():
    global remove
    remove = Toplevel()
    remove.wm_title("Remove RSS feed from File")
    for i in range(0, len(urls)):
        website = urls[i]
        # Create a var to hold TK command in, helps with callback looping problem (See button creation)
        removeCommand = lambda websiteURL=website: removeFeed(websiteURL)
        websiteButtons.append(ttk.Button(remove, text=website, command=removeCommand))
        websiteButtons[-1].pack(padx=30, pady=15)


def addFeed():
    global text
    # Open the file for appending and just write the new line to it
    new = newFeedGet.get()
    # If you're not subscribed already, subscribe!
    if new.strip() != "":
        if (new not in text):
            text.append(new)
            with open(path, 'a') as f:
                f.write(new + "\n")
            feed.destroy()
            refreshRSS()
    # Do this in two seperate places so that it can be executed before
    # refreshRSS() which is slow and makes it feel less responsive
    else:
        feed.destroy()


def refreshRSS():
    global websites, buttons, urls, text
    global addRSSButton, refreshRSSButton, noMoreEntries
    with open(path, 'r') as f:
        # Get rid of all the newlines while you're reading it in
        text = [x.strip() for x in f.readlines()]
    # Remove button needs to be added, tried to add it but was getting global errors. Will come back to it later.
    addRSSButton.pack_forget()
    refreshRSSButton.pack_forget()
    removeRSSButton.pack_forget()
    for site in websites:
        site.pack_forget()
    for button in buttons:
        button.pack_forget()
    for noMoreLabel in noMoreEntries:
        noMoreLabel.pack_forget()
    noMoreEntries = []
    websites = []
    buttons = []
    urls = []
    mainGUI(text)


# Functions to handle the hotkeys, need to pass "self" to these functions
# kind of a kludge, will request code review later.
# Just wanted to get it up and running
def refreshRSSBind(self):
    refreshRSS()


def addFeedBind(self):
    addFeedWindow()


def removeFeedBind(self):
    removeFeedWindow()


# Open sites.txt
try:
    with open(path, 'r') as f:
        # Get rid of all the newlines while you're reading it in
        text = [x.strip() for x in f.readlines()]
except:
    pass

mainGUI(text)
root.bind("-", removeFeedBind)
root.bind("+", addFeedBind)
root.bind('<F5>', refreshRSSBind)
root.mainloop()
