# Copyright 2017 Bloomberg Finance L.P.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock

ffi = mock.Mock()
lib = None

def ffi_typeof(type):
    if type == 'enum cdb2_errors':
        return mock.Mock(relements={'CDB2ERR_NOMASTER': -101, 'CDB2ERR_BADREQ': -17, 'CDB2ERR_VERIFY_ERROR': 2, 'CDB2ERR_DUPLICATE': 299, 'CDB2ERR_STOPPED': -16, 'CDB2ERR_IO_ERROR': -4, 'CDB2_OK': 0, 'CDB2ERR_INVALID_ID': -12, 'CDB2ERR_BADSTATE': -8, 'CDB2ERR_THREADPOOL_INTERNAL': -20, 'CDB2ERR_NOTSUPPORTED': 116, 'CDB2ERR_NULL_CONSTRAINT': 4, 'CDB2ERR_CONSTRAINTS': -103, 'CDB2ERR_BADCOLUMN': -7, 'CDB2ERR_INTERNAL': -5, 'CDB2ERR_DEADLOCK': 203, 'CDB2ERR_ACCESS': -106, 'CDB2ERR_NONKLESS': 114, 'CDB2ERR_TRAN_MODE_UNSUPPORTED': -107, 'CDB2ERR_READONLY': -21, 'CDB2ERR_MALLOC': 115, 'CDB2ERR_NOTCONNECTED': -2, 'CDB2ERR_TZNAME_FAIL': 401, 'CDB2ERR_UNTAGGED_DATABASE': -102, 'CDB2ERR_NOSTATEMENT': -6, 'CDB2_OK_DONE': 1, 'CDB2ERR_CONNECT_ERROR': -1, 'CDB2ERR_FKEY_VIOLATION': 3, 'CDB2ERR_PREPARE_ERROR': -3, 'CDB2ERR_DBCREATE_FAILED': -18, 'CDB2ERR_ASYNCERR': -9, 'CDB2ERR_REJECTED': -15, 'CDB2ERR_CONV_FAIL': 113, 'CDB2ERR_UNKNOWN': 300, 'CDB2ERR_RECORD_OUT_OF_RANGE': -13, 'CDB2_OK_ASYNC': -10, 'CDB2ERR_TRAN_IO_ERROR': -105})
    elif type == 'enum cdb2_coltype':
        return mock.Mock(relements={'CDB2_INTEGER': 1, 'CDB2_CSTRING': 3, 'CDB2_BLOB': 4, 'CDB2_DATETIME': 6, 'CDB2_REAL': 2, 'CDB2_DATETIMEUS': 9})
    elif type == 'enum cdb2_hndl_alloc_flags':
        return mock.Mock(relements={'CDB2_RANDOMROOM': 16, 'CDB2_RANDOM': 8, 'CDB2_ROOM': 32, 'CDB2_DIRECT_CPU': 4, 'CDB2_READ_INTRANS_RESULTS': 2})

ffi.typeof.side_effect = ffi_typeof
