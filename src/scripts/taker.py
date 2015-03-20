from xml.etree.ElementTree import parse

doc = parse('flicker.xml')
for photo in doc.findall("photo id"):
  