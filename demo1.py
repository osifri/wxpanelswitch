import wx


# PanelBase which is based on wx.Panel
# contains a common implementation for Panel1, Panel2, Panel3
# It draw a button in the center
# It accepts a background color, a label for the button and
# a callback function to call when the button is pressed
class PanelBase(wx.Panel):
    def __init__(self, parent, label, color, on_click):
        # Initialize the base class
        wx.Panel.__init__(self, parent=parent)
        # Create a vertical layout
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)
        # Create the button
        button = wx.Button(self, label=label)
        # Bind the button to the given callback
        button.Bind(wx.EVT_BUTTON, on_click)
        # Add space above the button
        sizer.Add((1, 1), 1, wx.EXPAND)
        # Add the button at the middle
        sizer.Add(button, 0, wx.ALIGN_CENTER)
        # Add space below the button
        sizer.Add((1, 1), 1, wx.EXPAND)
        # Set the background color
        self.SetBackgroundColour(color)


# Panel #1
class Panel1(PanelBase):
    def __init__(self, parent, on_click):
        PanelBase.__init__(self, parent, 'panel1',
                           (215, 252, 3), on_click)


# Panel #2
class Panel2(PanelBase):
    def __init__(self, parent, on_click):
        PanelBase.__init__(self, parent, 'panel2',
                           (215, 3, 252), on_click)


# Panel #3
class Panel3(PanelBase):
    def __init__(self, parent, on_click):
        PanelBase.__init__(self, parent, 'panel3',
                           (3, 215, 252), on_click)


# PanelsSwitcher is a type of BoxSizer which allows
# switching between panels
class PanelsSwitcher(wx.BoxSizer):
    # The constructor a parent window
    # and a list of panels for switch between them
    def __init__(self, parent, panels):
        # Initialize the base class
        wx.BoxSizer.__init__(self)
        # Attach this sizer to the parent window
        parent.SetSizer(self)
        # Save the parent windows
        self.parent = parent
        # Save the list of panels
        self.panels = panels
        # Add all the panels into this sizer
        for panel in self.panels:
            self.Add(panel, 1, wx.EXPAND)
        # Show the first panel and hide the rest of panels
        self.Show(panels[0])

    # Show some panel and hide the rest of panels
    def Show(self, panel):
        # For each panel in the list of panels
        for p in self.panels:
            # Show the given panel
            if p == panel:
                p.Show()
            else:
                # and hide the rest
                p.Hide()
        # Rearrange the window
        self.parent.Layout()


# MainFrame demonstrates how to use PanelsSwitcher for
# allowing switching between panels
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "PanelChanger Demo")
        # Create 3 demo panel
        self.panel1 = Panel1(self, self.on_click1)
        self.panel2 = Panel2(self, self.on_click2)
        self.panel3 = Panel3(self, self.on_click3)
        # Add them into a PanelsSwitcher
        self.panels_switcher = \
            PanelsSwitcher(
                self, [self.panel1, self.panel2, self.panel3])

    # Handler for the button in the first panel
    def on_click1(self, event):
        # Switch to the second panel
        self.panels_switcher.Show(self.panel2)

    # Handler for the button in the second panel
    def on_click2(self, event):
        # Switch to the third panel
        self.panels_switcher.Show(self.panel3)

    # Handler for the button in the third panel
    def on_click3(self, event):
        # Switch to the first panel
        self.panels_switcher.Show(self.panel1)


if __name__ == '__main__':
    # Create a wx application
    app = wx.App()
    # Create the demo window
    win = MainFrame()
    # Show the window
    win.Show()
    # Start wx main loop
    app.MainLoop()
