#!/usr/bin/env python

from pptx import Presentation
from parser import *
from reavelparser import *
import sys
from lxml.html import tostring

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print "arg error , commonds should: doit filename outfilename"
    
    sectionlist = parse_reveal_html5(sys.argv[1])
    eparser = Etree2pptx()
    prs = Presentation()

    eparser.headsection2pptx( prs, sectionlist[0])
    for sec in sectionlist[1:]:
        eparser.parse_section2pptx(prs,sec)

    prs.save(sys.argv[2])

   # print tostring(sectionlist[1])
