__author__ = 'Carter'
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
from django.contrib.auth.models import User

# INITIALIZATION SCRIPT FOR CHF DATABASE

delUser = User.objects.all()
delUser.delete()
delClient = cMod.Client.objects.all()
delClient.delete()


# MAKE USER 1
user = User.objects.create_user('hesto2', 'hestermancarter@gmail.com', 'password1')
user.last_name = 'Hesterman'

carter = cMod.Client()
parish = cMod.Client()
trevor = cMod.Client()
sam = cMod.Client()

carter.address = "3289 Mohawk Circle"
carter.zip = "84064"
carter.city = "Provo"
carter.state = "UT"
carter.securityQuestion = "Mother's maiden name?"
carter.securityAnswer = "Jane"
carter.phoneNumber = "8018341490"
carter.user = user
# carter.photo = "/CHF/media/carterPhoto.JPG"

carter.save()
user.save()


# MAKE USER 2
user = User.objects.create_user('parishHansen6', 'parishhansen@gmail.com', 'password1')
user.last_name = 'Hansen'

parish.address = "111 s. 350 e."
parish.zip = "84062"
parish.city = "Provo"
parish.state = "UT"
parish.securityQuestion = "Father's maiden name?"
parish.securityAnswer = "Skywalker"
parish.phoneNumber = "5722708945"
parish.user = user
# parish.photo = "/CHF/media/carterPhoto.JPG"

parish.save()
user.save()

# MAKE USER 3
user = User.objects.create_user('tBone', 'trevorJones717@gmail.com', 'password1')
user.last_name = 'Jones'

trevor.address = "500 s. 450 w."
trevor.zip = "84062"
trevor.city = "Provo"
trevor.state = "UT"
trevor.securityQuestion = "Favorite Color?"
trevor.securityAnswer = "Purple"
trevor.phoneNumber = "3584655001"
trevor.user = user
# trevor.photo = "/CHF/media/carterPhoto.JPG"

trevor.save()
user.save()


# MAKE USER 4
user = User.objects.create_user('lucey', 'samlucero6@gmail.com', 'password1')
user.last_name = 'Jones'

sam.address = "200 s. 400 w."
sam.zip = "84062"
sam.city = "Provo"
sam.state = "UT"
sam.securityQuestion = "Favorite Color?"
sam.securityAnswer = "Mauve"
sam.phoneNumber = "46540025462"
sam.user = user
# sam.photo = "/CHF/media/carterPhoto.JPG"

sam.save()
user.save()

print("Users Initialized")