#!/usr/bin/env python
# -*- coding: utf-8 -*-#
#
#
# Copyright (C) 2018 University of Zurich. All rights reserved.
#
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import pytest
from flask import session

from api.account import add_account
from db.account import Account
from db.handler import init_db


@pytest.fixture()
def initialize():
    init_db("sqlite://")


def test_admin_can_create_account():
    session['admin'] = True
    result, code = add_account(Account(name='test', principle_investigator='test_pi'))
    assert code == 201
    assert result is not None
    assert result.id is not None
    assert result.name == 'test'

