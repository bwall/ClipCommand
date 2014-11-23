#!/usr/bin/env python2
import pygtk

pygtk.require('2.0')
import gtk
import gtk.glade

import subprocess
import threading
import os


def execute_command_with_string_as_stdin(command, data):
    try:
        ret = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        (out, err) = ret.communicate(input=data)
        if out.endswith("\n"):
            out = out[:-1]
        return out
    except:
        return None


def clipboard_execute(clipboard, command, clip_data, exit_when_done=True):
    text = execute_command_with_string_as_stdin(command, clip_data)
    gtk.threads_enter()
    clipboard.set_text(text)
    gtk.threads_leave()
    if exit_when_done:
        gtk.threads_enter()
        gtk.main_quit()
        gtk.threads_leave()


def invoke_exec_thread(clipboard, text, command):
    t = threading.Thread(target=clipboard_execute, args=(clipboard, command, text, True))
    t.start()


def exec_and_abandon(command):
    os.system("{0} &".format(command))
    gtk.main_quit()


class ClipboardCommandInput:
    def __init__(self):
        # Set the Glade file
        self.gladefile = '<?xml version="1.0" encoding="UTF-8"?>' \
                         '<interface>' \
                         '<requires lib="gtk+" version="2.24"/>' \
                         '<!-- interface-naming-policy project-wide -->' \
                         '<object class="GtkWindow" id="MainWindow">' \
                         '<property name="can_focus">False</property>' \
                         '<property name="title" translatable="yes">ClipCommand</property>' \
                         '<child>' \
                         '<object class="GtkVBox" id="vbox1">' \
                         '<property name="visible">True</property>' \
                         '<property name="can_focus">False</property>' \
                         '<child>' \
                         '<object class="GtkEntry" id="commandEntry">' \
                         '<property name="visible">True</property>' \
                         '<property name="can_focus">True</property>' \
                         '<property name="invisible_char">-</property>' \
                         '<property name="shadow_type">none</property>' \
                         '<property name="primary_icon_activatable">False</property>' \
                         '<property name="secondary_icon_activatable">False</property>' \
                         '<property name="primary_icon_sensitive">True</property>' \
                         '<property name="secondary_icon_sensitive">True</property>' \
                         '<signal name="key-press-event" handler="on_commandEntry_key_press_event" swapped="no"/>' \
                         '</object>' \
                         '<packing>' \
                         '<property name="expand">True</property>' \
                         '<property name="fill">True</property>' \
                         '<property name="position">0</property>' \
                         '</packing>' \
                         '</child>' \
                         '<child>' \
                         '<object class="GtkButton" id="buttonCancel">' \
                         '<property name="label" translatable="yes">Cancel</property>' \
                         '<property name="visible">True</property>' \
                         '<property name="can_focus">True</property>' \
                         '<property name="receives_default">True</property>' \
                         '<signal name="clicked" handler="on_buttonCancel_clicked" swapped="no"/>' \
                         '</object>' \
                         '<packing>' \
                         '<property name="expand">True</property>' \
                         '<property name="fill">True</property>' \
                         '<property name="position">1</property>' \
                         '</packing>' \
                         '</child>' \
                         '</object>' \
                         '</child>' \
                         '</object>' \
                         '</interface>'

        self.glade = gtk.Builder()
        self.glade.add_from_string(self.gladefile)
        self.glade.connect_signals(self)
        self.glade.get_object("MainWindow").show_all()
        window = self.glade.get_object("MainWindow")
        if window:
            window.connect("destroy", gtk.main_quit)

    def on_buttonCancel_clicked(self, widget):
        gtk.main_quit()

    def on_commandEntry_key_press_event(self, one, event):
        if event.keyval == 65293:
            command_entry = self.glade.get_object("commandEntry")
            command = command_entry.get_text()
            clipboard = gtk.clipboard_get()
            clipboard.request_text(invoke_exec_thread, command)


if __name__ == "__main__":
    gtk.gdk.threads_init()
    hwg = ClipboardCommandInput()
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()

