import json
from commonwealth import *

def testGetUnits():
    data = getUnits()
    assert data != None
    assert data.startswith("jQuery")

def testParseUnits():
    testJson = {
        "bristol": [101, 102, 103],
        "hamilton": [512]
    }
    # convert to a string
    testJson = json.dumps(testJson)
    availableUnits = parseUnits(testJson)
    assert availableUnits == testJson

def testParseUnitsDirty():
    testJson = {
        "bristol": [101, 102, 103],
        "hamilton": [512]
    }
    # convert to a string
    testJson = json.dumps(testJson)
    testJsonDirty = f"jQuery22408679066000885238_1668731524273({testJson})"
    availableUnits = parseUnits(testJsonDirty)
    assert availableUnits == testJson

def testIntegration():
    data = getUnits()
    assert data != None
    assert data.startswith("jQuery")
    availableUnits = parseUnits(data)
    assert availableUnits.startswith("{")
    assert availableUnits.endswith("}")