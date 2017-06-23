// Fill out your copyright notice in the Description page of Project Settings.

#include "UE4Protobuf.h"
#include "UE4ProtobufGameModeBase.h"
#include "Proto/Test.pb.h"

AUE4ProtobufGameModeBase::AUE4ProtobufGameModeBase()
{
	SearchRequest Request;

	Request.set_query("test");
	Request.set_page_number(1);
	Request.set_result_per_page(2);
}


