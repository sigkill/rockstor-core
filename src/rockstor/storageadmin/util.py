"""
Copyright (c) 2012-2013 RockStor, Inc. <http://rockstor.com>
This file is part of RockStor.

RockStor is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

RockStor is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from storageadmin.exceptions import RockStorAPIException
from system.osi import run_command
from django.conf import settings

import logging
logger = logging.getLogger(__name__)

def handle_exception(e, request):
    logger.error('request path: %s method: %s data: %s' %
                 (request.path, request.method, request.DATA))
    logger.exception('exception: %s' % e.__str__())
    run_command(['/usr/bin/tar', '-c', '-z', '-f',
                     settings.ROOT_DIR + 'src/rockstor/logs/error.tgz',
                     settings.ROOT_DIR + 'var/log'])
    raise RockStorAPIException(detail=e.__str__())
