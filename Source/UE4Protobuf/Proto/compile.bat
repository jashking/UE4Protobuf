@echo off

..\..\Protobuf\bin\protoc.exe --proto_path=. --cpp_out=. Test.proto

pause