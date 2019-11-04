#!/usr/bin/python

from strip_accents import text_to_id
import hashlib


def generate_GUID(keyInput):

    key = keyInput
    keygood = text_to_id(key)
    GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()
    return GUID
