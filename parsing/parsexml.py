# Fill in this file with the code from parsing XML exercise
import xml.etree.ElementTree as ET
import re
xml= ET.parse("myfile.xml")
root = xml.getroot()
ns = re.match('{.*}',root.tag).group(0)
editconfig = root.find('{}edit-config'.format(ns))
defop = editconfig.find('{}default-operation'.format(ns))
testop =editconfig.find("{}test-option".format(ns))
print('La default-operation contiene: {}'.format(defop.text))
print('La test-option contiene: {}'.format(testop.text))