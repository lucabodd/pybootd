# Copyright (c) 2010-2019 Emmanuel Blot <emmanuel.blot@free.fr>
# Copyright (c) 2010-2011 Neotion
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import os

__version__ = '1.7.0'


def pybootd_path(path):
    newpath = ''
    if path.startswith(os.sep):
        newpath = path
    elif os.path.exists(path):
        newpath = path
    else:
        from pkg_resources import DistributionNotFound
        try:
            from pkg_resources import Requirement, resource_filename
            from pkg_resources import get_distribution
        except ImportError:
            raise IOError('pkg_resources module not available')
        try:
            newpath = resource_filename(Requirement.parse('pybootd'), path)
            if not newpath:
                localpath = get_distribution('pybootd').location
                newpath = os.path.join(localpath, path)
        except DistributionNotFound:
            newpath = path
        except KeyError:
            raise IOError('No such file or directory (resource)')
    if not os.path.isfile(newpath) and not os.path.isdir(newpath):
        raise IOError('No such file or directory (local)')
    return newpath
