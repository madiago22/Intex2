__author__ = 'Carter'

#!/usr/bin/env python3
import os
from django.db.models import Avg,Max,Min
# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'

import django
django.setup()

import CHF.models as cMod


# INITIALIZATION SCRIPT FOR CHF DATABASE
# MAKE USER 1

cMod.Client.objects.all().delete()

user = cMod.Client()
user.last_name = "Hesterman"
user.password = "password1"
user.email ="hestermancarer@gmail.com"
user.first_name = "Carter"
user.address = "3289 Mohawk Circle"
user.zip = "84064"
user.city = "Provo"
user.state = "UT"
user.securityQuestion = "Mother's maiden name?"
user.securityAnswer = "Jane"
user.phoneNumber = "8018341490"
user.username = "hesto2"
user.save()

user = cMod.Client()
user.last_name = "Lucero"
user.password = "password1"
user.email ="samlucero@gmail.com"
user.first_name = "Sam"
user.address = "151 s 100 e Starling way"
user.zip = "84064"
user.city = "Provo"
user.state = "UT"
user.securityQuestion = "Mother's maiden name?"
user.securityAnswer = "Gomez"
user.phoneNumber = "2708805987"
user.username = "lucey"
user.save()

user = cMod.Client()
user.last_name = "Jones"
user.password = "password1"
user.email ="trevoerjones717@gmail.com"
user.first_name = "Trevor"
user.address = "3 Silicon Way"
user.zip = "90080"
user.city = "Simi Valley"
user.state = "CA"
user.securityQuestion = "Mother's maiden name?"
user.securityAnswer = "Ciobatta"
user.phoneNumber = "4658054567"
user.username = "tBone"
user.save()

user = cMod.Client()
user.last_name = "Hansen"
user.password = "password1"
user.email ="parishhansen@gmail.com"
user.first_name = "Parish"
user.address = "500 s Provo Way"
user.zip = "84064"
user.city = "Provo"
user.state = "UT"
user.securityQuestion = "Mother's maiden name?"
user.securityAnswer = "Smith"
user.phoneNumber = "6458245468"
user.username = "PAPA"
user.save()

print("Users Initialized")