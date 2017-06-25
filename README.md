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

### 修改 libprotobuf 源码 ###

主要是去掉两个宏开关 `GOOGLE_PROTOBUF_NO_RTTI` 和 `HAVE_PTHREAD`

#### 去掉 HAVE_PTHREAD 宏 ####

在非 `Windows` 平台下都要打开 `HAVE_PTHREAD` 宏

打开 `google/protobuf/stubs/common.cc`，把两个地方的 `elif defined(HAVE_PTHREAD)` 改成 `#else`

并且把第一处以下两行代码删除

``` cpp
#else
#error "No suitable threading library available."
```

#### 去掉 GOOGLE_PROTOBUF_NO_RTTI 宏 ####

在所有平台下都要禁用 `RTTI`，因为 `UE4` 禁用了 `C++` 的运行时类型识别(`typeid` 和 `dynamic_cast`)

打开 `google/protobuf/arena.h`，将

``` cpp
#ifndef GOOGLE_PROTOBUF_NO_RTTI
#define RTTI_TYPE(type) (&typeid(type))
#else
#define RTTI_TYPE_ID(type) (NULL)
#endif
```

改为

``` cpp
#define RTTI_TYPE_ID(type) (NULL)
```

打开 `google/protobuf/generated_message_reflection.h`，将

``` cpp
#if defined(GOOGLE_PROTOBUF_NO_RTTI) || (defined(_MSC_VER)&&!defined(_CPPRTTI))
	return NULL;
#else
	return dynamic_cast<To>(from);
#endif
```

改为

``` cpp
return NULL;
```

将

``` cpp
#if defined(GOOGLE_PROTOBUF_NO_RTTI) || (defined(_MSC_VER)&&!defined(_CPPRTTI))
	bool ok = &T::default_instance9) == from->GetReflection()->GetMessageFactory()->GetPrototype(from->GetDescriptor());
		return ok ? down_cast<T*>(from) : NULL;
#else
	return dynamic_cast<To>(from);
#endif
```

改为

``` cpp
bool ok = &T::default_instance9) == from->GetReflection()->GetMessageFactory()->GetPrototype(from->GetDescriptor());
return ok ? down_cast<T*>(from) : NULL;
```

打开 `google/protobuf/stubs/casts.h`，删除以下两处代码

``` cpp
#if !defined(NDEBUG) && !defined(GOOGLE_PROTOBUF_NO_RTTI)
	assert(f == NULL || dynamic_cast<To>(f) != NULL); // RTTI: debug mode only!
#endif
```

和

``` cpp
#if !defined(NDEBUG) && !defined(GOOGLE_PROTOBUF_NO_RTTI)
	// RTTI: debug mode only!
	assert(dynamic_cast<ToAsPointer>(&f) != NULL); 
#endif
```

### 禁用编译警告 ###

因为 `UE4` 会将一些编译警告当成错误，所以要将编译过程中 `libprotobuf` 中的警告禁用掉
