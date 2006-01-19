# Copyright (C) 2005 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Gaupol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gaupol; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


"""Cell renderer for cells containing multiline text."""


try:
    from psyco.classes import *
except ImportError:
    pass

import gtk

from gaupol.gtk.cellrend.text import CellRendererText


class CellTextView(gtk.TextView, gtk.CellEditable):

    """Text view that implements gtk.CellEditable."""

    __gtype_name__ = 'CellTextView'

    def do_editing_done(self, *args):
        """End editing by removing the editor."""

        self.remove_widget()

    def do_remove_widget(self, *args):
        """Empty method to avoid console error output."""
        pass

    def do_start_editing(self, *args):
        """Empty method to avoid console error output."""
        pass

    def get_text(self, *args):
        """Get the text."""

        text_buffer = self.get_buffer()
        start, end = text_buffer.get_bounds()
        return text_buffer.get_text(start, end, True)

    def set_text(self, text):
        """Set the text."""

        self.get_buffer().set_text(text)


class CellRendererMultilineText(CellRendererText):

    """Cell renderer for cells containing multiline text."""

    def on_start_editing(self, event, widget, row, background_area, cell_area,
                         flags):
        """
        Initiate editing of the cell.

        Return: CellTextView
        """
        editor = CellTextView()
        editor.set_wrap_mode(gtk.WRAP_NONE)
        editor.modify_font(self.font_description)

        editor.set_text(self.text or u'')

        editor.connect('editing-done'   , self.on_editing_done   , row)
        editor.connect('key-press-event', self.on_key_press_event     )

        editor.grab_focus()
        editor.show()
        return editor

    def on_key_press_event(self, editor, event):
        """
        Respond to key press events.

        End editing if Return, Keypad Enter or Escape pressed. Shift or Control
        combined with Return or Keypad Enter can be used for linebreaking.
        Escape cancels editing.
        """
        accel_masks = (gtk.gdk.CONTROL_MASK|gtk.gdk.SHIFT_MASK)
        keymap = gtk.gdk.keymap_get_default()

        args = event.hardware_keycode, event.state, event.group
        output = keymap.translate_keyboard_state(*args)
        keyval, egroup, level, consumed = output
        keyname = gtk.gdk.keyval_name(keyval)

        if event.state & ~consumed & accel_masks:
            return

        if keyname in ('Return', 'KP_Enter'):
            editor.emit('editing-done')
            return True

        if keyname == 'Escape':
            editor.remove_widget()
            self.emit('editing-canceled')
            return True