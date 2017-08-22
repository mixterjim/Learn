#!/usr/bin/env python
# -*- coding: utf-8 -*-
A = int(input(u"Please input you Age:"))  # Integer
a = 12
name = input('Please input you name:')
# str(name)  # String
print("Hi %s,your chinese zodiac anniversary year will become %02d years later." % (name, (12-A % a)))
print("You name used %.1f%% byte" % (len(name)*100))
