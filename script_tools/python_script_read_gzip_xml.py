#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cStringIO
import xml.etree.ElementTree as ET

gzip_file = gzip.open(file_name, 'rb');
xml_file_in_memory = cStringIO.StringIO(gzip_file.read())