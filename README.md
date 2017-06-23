# UE4Protobuf

A protobuf source integration for UE4.

直接在项目中集成 `libprotobuf` 的源码，方便使用

## 测试平台 ##

* 已测试通过
	* `Win32`, `Win64`
	* `Android`

* 未测试
	* `Linux`
	* `Mac`
	
## 如何使用 ##

直接将 `google` 文件夹复制到自己的项目源码目录下，并且复制 `UE4Protobuf.Build.cs` 文件中的 `Definitions` 到自己项目的 `.Build.cs` 文件中

## 以下记录完整步骤 ##

### 提取 libprotobuf 源码 ###

* 到 [protobuf releases](https://github.com/google/protobuf/releases)下载 `protobuf-cpp` 源码包
* 用 `CMake` 生成 `Visual Studio` 工程

``` bash
cd /D protobuf-3.2.0\cmake

cmake.exe -G "Visual Studio 14 2015 Win64" .
```

* 将工程 `libprotobuf` 中用到的源码文件和对应的头文件提取出来

### 在UE4工程中使用libprotobuf源码 ###

* 将提取的 `libprotobuf` 源码放到工程源码目录下
* 在工程的 `.Build.cs` 中增加 `Definitions`

``` cpp
// Protobuf source integrationg
Definitions.Add("GOOGLE_PROTOBUF_NO_RTTI");
if (Target.Platform == UnrealTargetPlatform.Win32 || Target.Platform == UnrealTargetPlatform.Win64)
{
	Definitions.Add("_CRT_SECURE_NO_WARNINGS");
}
else if (Target.Platform == UnrealTargetPlatform.Android || Target.Platform == UnrealTargetPlatform.Linux)
{
	Definitions.Add("HAVE_PTHREAD=1");
}
```

### 禁用编译警告 ###

因为 `UE4` 会将一些编译警告当成错误，所以要将编译过程中 `libprotobuf` 中的警告禁用掉
