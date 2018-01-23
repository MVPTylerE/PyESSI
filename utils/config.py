# -*- coding: utf-8 -*-
"""
Created Jan 2018

@author: Hao Chen

Functions:


"""

#pyESSI Project Setup
#[ProjectSetup]
workSpace = 'D:\GaohrWS\DoctorWorks\DoctorWork\PyESSI\PyESSI\DCBAM'
startTime = 19960101
endTime = 20001231

#pyESSI GridIO File
#[GridIO]
DEMFileName = 'YLXDem240.tif'
LULCFileName = 'YLXLulc240.tif'
SoilFileName = 'YLXSoil240.tif'

#PyESSI Model Running Parameters
#[RunPara]
PETMethod = 4
AETMethod = 2
InterpMethod = 1
AIMethod = 1
DLAICalcMethod = 3
RunoffSimuType = 2
SurfRouteMethod = 1
LatRouteMethod = 1
BaseRouteMethod = 1
RiverRouteMethod = 1
InfilCurveType = 1

#PyESSI Model Input Parameters
#[InputPara]
GSKv = 4000.00
GLKv = 1500.00
GBKv = 1200.00
GRKv = 0.00
LowWaterSurfQLoss = 22.50
MidWaterSurfQLoss = 24.00
HighWaterSurfQLoss = 48.00
LatQLoss = 15.00
BaseQLoss = 13.50
RiverQLoss = 0.00
RiverProType = 2
RiverProWidth = 20.00
HillProType = 4
HillProWidth = 240.00
SMCTimeWeight = -0.40
SMCGridRTravelTime = 2.80
LMCTimeWeight = 0.10
LMCGridRTravelTime = 10.00
BMCTimeWeight = -0.60
BMCGridRTravelTime = 4.00
SurfQLinearFactor = 1.00
SurfQOutFactor = 0.90
LatQOutFactor = 0.50
DailyMeanPcpTime = 2.00
SnowTemperature = 1.00
DDF = 0.40
DeepBaseQ = 10.00

#PyESSI Model MidGridOut Parameters
#[MidGridOut]
strOutBDate = 19960101
strOutEDate = 20001231
iPcp = 0
iTempMax = 0
iTempMin = 0
iTempMean = 0
iSlr = 0
iHmd = 0
iWnd = 0
iPET = 0
iAET = 0
iCI = 0
iSnowWater = 0
iAI = 0
iRouteOut = 0
iSurfQ = 0
iLatQ = 0
iBaseQ = 0
iInfilRate = 0
iWaterYieldType = 0
iProfileSoilWater = 0
iAvgSoilWater = 0


