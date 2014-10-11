#!/usr/bin/env python

from lxml.html import tostring, html5parser
import re

def clear_tag(tag):
    return re.sub(r'\{.*\}','',tag)


def parse_reveal_html5( fname):
    
    lp = html5parser.parse(fname)
    root = lp.getroot()
    root = root[1][0][0]
    
    return root.getchildren()
