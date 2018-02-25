import xml.etree.ElementTree as ET
import os
import shutil

LibProtobufFilterPath = 'D:/Test/protobuf-3.5.1/libprotobuf.vcxproj.filters'
CurrentPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'google\\protobuf')

Tree = ET.ElementTree(file='D:/Test/protobuf-3.5.1/libprotobuf.vcxproj.filters')
Root = Tree.getroot()
for ItemGroup in Root:
    for Child in ItemGroup:
        if 'ClCompile' in Child.tag or 'ClInclude' in Child.tag:
            SourceFile = Child.attrib['Include']
            TargetFile = os.path.join(CurrentPath, SourceFile[SourceFile.rfind('protobuf\\') + 9 :])
            TargetPath = TargetFile[:TargetFile.rfind('\\')]
            if not os.path.exists(TargetPath):
                os.makedirs(TargetPath)
            shutil.copyfile(SourceFile, TargetFile)
            print 'copied ', SourceFile
            