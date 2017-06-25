// Fill out your copyright notice in the Description page of Project Settings.

using UnrealBuildTool;
using System.Collections.Generic;

public class UE4ProtobufTarget : TargetRules
{
	public UE4ProtobufTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		
		ExtraModuleNames.AddRange( new string[] { "UE4Protobuf" } );
	}
}
