#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from strip_accents import text_to_id
import hashlib
import re
import datetime


def generate_GUID2(
    nom,
    prenom,
    age,
    sexe,
    ):

    if '-' in age:
        if re.match("^[0-9]{2}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%d-%m-%Y').strftime('%d-%m-%Y')
            key = nom + prenom + date_time_obj + sexe

            keygood = text_to_id(key)

            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID

        if re.match("^[0-9]{4}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%Y-%m-%d').strftime('%d-%m-%Y')
            key = nom + prenom + date_time_obj + sexe
            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()
            return GUID

    if '/' in age:
        if re.match("^[0-9]{2}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%d/%m/%Y').strftime('%d/%m/%Y')

            key = nom + prenom + date_time_obj + sexe

            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID

        if re.match("^[0-9]{4}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%Y/%m/%d').strftime('%d/%m/%Y')

            key = nom + prenom + date_time_obj + sexe

            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID

    if r"\\" in age:
        if re.match("^[0-9]{2}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%d\%m\%d').strftime('%d\%m\%Y')

            key = nom + prenom + date_time_obj + sexe

            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID

        if re.match("^[0-9]{4}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%Y\%m\%d').strftime('%d\%m\%Y')

            key = nom + prenom + date_time_obj + sexe

            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID

    if ' ' in age:
        if re.match("^[0-9]{2}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%d %m %Y').strftime('%d %m %Y')

            key = nom + prenom + date_time_obj + sexe
            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID

        if re.match("^[0-9]{4}\D", age):
            date_time_str = str(age)
            date_time_obj = datetime.datetime.strptime(date_time_str,
                    '%Y %m %d').strftime('%d %m %Y')

            key = nom + prenom + date_time_obj + sexe
            keygood = text_to_id(key)
            GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

            return GUID
    else:

        key = nom + prenom + age + sexe
        keygood = text_to_id(key)
        GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

        return GUID


def generate_GUID(keyInput):

    key = keyInput
    keygood = text_to_id(key)
    GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()
    return GUID
