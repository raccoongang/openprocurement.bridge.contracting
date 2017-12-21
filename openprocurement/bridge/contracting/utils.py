from uuid import uuid4


def generate_req_id():
    return b'contracting-data-bridge-req-' + str(uuid4()).encode('ascii')


def journal_context(record=None, params=None):
    if record is None:
        record = {}
    if params is None:
        params = {}
    for k, v in params.items():
        record["JOURNAL_" + k] = v
    return record

