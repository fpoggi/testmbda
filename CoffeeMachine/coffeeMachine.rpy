I-Logix-RPY-Archive version 8.8.0 C++ 6103821
{ IProject 
	- _id = GUID 80800b57-4175-4d88-a0b1-d2cb14f01787;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 3;
			- value = 
			{ IPropertySubject 
				- _Name = "Activity_diagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "DefaultTransition";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "ObjectModelGe";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Association";
						- Properties = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowSourceMultiplicity";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowSourceQualifier";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowSourceRole";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "ShowTargetMultiplicity";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowTargetQualifier";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowTargetRole";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Link";
						- Properties = { IRPYRawContainer 
							- size = 7;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowSourceMultiplicity";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowSourceRole";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "ShowTargetMultiplicity";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowTargetRole";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "PanelDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Led";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name_only";
								- _Type = Enum;
								- _ExtraTypeInfo = "";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "PushButton";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name_only";
								- _Type = Enum;
								- _ExtraTypeInfo = "";
							}
						}
					}
				}
			}
		}
	}
	- _name = "coffeeMachine";
	- _modifiedTimeWeak = 5.22.2013::10:56:44;
	- _lastID = 2;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "CoffeePackage.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "CoffeePackage";
		- _id = GUID 54eadf93-d640-4094-ae78-e7075b59ef06;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "CoffeMachineComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "CoffeMachineComponent";
		- _id = GUID d0c9c3d8-296c-4a01-858f-80f5e1888664;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 3;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ ISubsystem 
			- fileName = "CoffeePackage";
			- _id = GUID 54eadf93-d640-4094-ae78-e7075b59ef06;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID a089e243-a691-4c92-96d6-51f12c5334b5;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "DefaultTransition";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Link";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Underline";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Model Overview";
			- _modifiedTimeWeak = 1.1.1970::2:0:0;
			- _lastModifiedTime = "6.7.2011::16:26:53";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 8cddd5fe-f000-4f05-b5f6-97f45b0ec476;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID a089e243-a691-4c92-96d6-51f12c5334b5;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 2;
				{ CGIClass 
					- _id = GUID 92168990-a405-49a0-8b8d-1c164413af1f;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "CoffeePackage.sbs";
						- _subsystem = "CoffeePackage";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID ae5cd1d9-bb3c-4bbd-a6b6-24e0d32d527a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 8970f72c-249d-4cce-ae21-65a0f50bb8e7;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 3f1df323-578e-4e50-9337-b0a197fadbf4;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 679d0af7-c615-4d22-8b92-06b66101d109;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "CoffeePackage.sbs";
						- _subsystem = "CoffeePackage";
						- _class = "";
						- _name = "comment_11";
						- _id = GUID 377717ee-126b-4767-98c3-f41c1ef3ad80;
					}
					- m_pParent = GUID 92168990-a405-49a0-8b8d-1c164413af1f;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.712177 0 0 0.389195 46 51 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 92168990-a405-49a0-8b8d-1c164413af1f;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "CoffeePackage.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "CoffeePackage";
				- _id = GUID 54eadf93-d640-4094-ae78-e7075b59ef06;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "CoffeMachineComponent";
			- _id = GUID d0c9c3d8-296c-4a01-858f-80f5e1888664;
		}
	}
}

