#coding: utf-8

from xml import sax



class Handler(sax.handler.ContentHandler):
    def startElement(self, name, attrs):


    def endElement(self, name):


    def characters(self, content):


parser = sax.make_parser()
parser.setContentHandler(Handler())
parser.parse("neko.txt.cabocha")
