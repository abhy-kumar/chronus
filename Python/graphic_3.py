import os, sys, re, time
import wx
from wx.lib.splitter import MultiSplitterWindow
from General_feed_extract import FeedsReader
import wx.lib.scrolledpanel as scrolled


class SamplePane(scrolled.ScrolledPanel):
    """
    Just a simple test window to put into the splitter.
    Set to scrollable, set to word wrap
    """

    def __init__(self, parent, label):
        scrolled.ScrolledPanel.__init__(self, parent, style=wx.BORDER_SUNKEN)
        # self.SetBackgroundColour(colour)
        self.textbox = wx.TextCtrl(self, -1, label, style=wx.TE_MULTILINE)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.textbox, 1, wx.ALIGN_LEFT | wx.ALL | wx.EXPAND, 5)
        self.SetSizer(vbox)
        self.SetAutoLayout(1)
        self.SetupScrolling()

        self.SetupScrolling()

    def SetOtherLabel(self, label):
        self.textbox.SetValue(label)
        self.SetupScrolling()


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.parent = parent

        ## Add in the feeds parameters
        self.reader = FeedsReader()

        ## Add in timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer_update_feeds, self.timer)
        self.timer.Start(30000)  # start timer after a delay, time in milli sec

        splitter = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        self.splitter = splitter
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.world_news_panel = SamplePane(splitter, "Panel One")
        splitter.AppendWindow(self.world_news_panel, 140)

        self.SG_panel = SamplePane(splitter, "Panel Two")
        # self.SG_panel.SetMinSize(self.SG_panel.GetBestSize())
        splitter.AppendWindow(self.SG_panel, 180)

        self.others_panel = SamplePane(splitter, "Panel Three")
        splitter.AppendWindow(self.others_panel, 105)

        ## Set the orientation
        self.splitter.SetOrientation(wx.VERTICAL)

        ## Updates the panel
        self.update_panels()

    def get_feeds(self):
        """ Run the get feeds class. Use for getting updates of the feeds.

        """
        self.reader.parse_rss_sites_by_cat()

    def update_panels(self):
        """ Update all the panels with the updated feeds.
            Can use the set other label method

        """
        self.get_feeds()
        self.update_SG_panel()
        self.update_world_panel()

    def update_world_panel(self):
        """ Update World_panel on the World news.

        """
        date_key = self.reader.set_last_desired_date(0)
        if self.reader.rss_results_dict_by_cat['World'].has_key(date_key):
            World_news_list = self.reader.rss_results_dict_by_cat['World'][date_key]
            World_news_str = '\n********************\n'.join(['\n'.join(n) for n in World_news_list])
            self.world_news_panel.SetOtherLabel(World_news_str)

    def update_SG_panel(self):
        """ Update SG_panel on the Singapore stock news.

        """
        date_key = self.reader.set_last_desired_date(0)
        if self.reader.rss_results_dict_by_cat['SG'].has_key(date_key):
            SG_news_list = self.reader.rss_results_dict_by_cat['SG'][date_key]
            SG_news_str = '\n********************\n'.join(['\n'.join(n) for n in SG_news_list])
            self.SG_panel.SetOtherLabel(SG_news_str)

    def on_timer_update_feeds(self, evt):
        """ Update feeds once timer reach.
        """
        print
        'Updating....'
        self.update_panels()

    def SetLiveUpdate(self, enable):
        if enable:
            self.splitter.SetWindowStyle(wx.SP_LIVE_UPDATE)
        else:
            self.splitter.SetWindowStyle(0)


class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, pos=(150, 20), size=(850, 720))  # size and position

        self.top_panel = MyPanel(self)


class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)
        self.frame = MyFrame(None, wx.ID_ANY, "Feeds Watcher")
        self.SetTopWindow(self.frame)

        self.frame.Show()

app.Mainloop()


if __name__ == "__main__":
    run()