# Copyright (C) 2005-2006 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA 02110-1301, USA.


"""All subtitle file format classes."""


from gaupol.base.file.ass        import AdvancedSubStationAlpha
from gaupol.base.file.microdvd   import MicroDVD
from gaupol.base.file.mpl2       import MPL2
from gaupol.base.file.mpsub      import MPsub
from gaupol.base.file.ssa        import SubStationAlpha
from gaupol.base.file.subrip     import SubRip
from gaupol.base.file.subviewer2 import SubViewer2


__all__ = [
    'AdvancedSubStationAlpha',
    'MPL2',
    'MicroDVD',
    'MPsub',
    'SubRip',
    'SubStationAlpha',
    'SubViewer2',
]