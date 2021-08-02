# Python 3.9.0

# AveragedTimeOfTravel

def AveragedTimeOfTravel(

    P1FractionOfPeriodPerPeriod,
    P1BPeriod,
    P1BDistance,
    P1APeriod,
    P1ADistance,

    P2FractionOfPeriodPerPeriod,
    P2BPeriod,
    P2BDistance,
    P2APeriod,
    P2ADistance,

    P3FractionOfPeriodPerPeriod,
    P3BPeriod,
    P3BDistance,
    P3APeriod,
    P3ADistance,

    P4FractionOfPeriodPerPeriod,
    P4BPeriod,
    P4BDistance,
    P4APeriod,
    P4ADistance,

    P5FractionOfPeriodPerPeriod,
    P5BPeriod,
    P5BDistance,
    P5APeriod,
    P5ADistance,

    P6FractionOfPeriodPerPeriod,
    P6BPeriod,
    P6BDistance,
    P6APeriod,
    P6ADistance

    ):

    '''

    '''

    PulsarOne = {
        "FractionOfPeriodPerPeriod" : P1FractionOfPeriodPerPeriod,
        "BeforePeriod" : P1BPeriod,
        "BeforeDistance" : P1BDistance,
        "AfterPeriod" : P1APeriod,
        "AfterDistance" : P1ADistance
        }

    PulsarTwo = {
        "FractionOfPeriodPerPeriod" : P2FractionOfPeriodPerPeriod,
        "BeforePeriod" : P2BPeriod,
        "BeforeDistance" : P2BDistance,
        "AfterPeriod" : P2APeriod,
        "AfterDistance" : P2ADistance
        }

    PulsarThree = {
        "FractionOfPeriodPerPeriod" : P3FractionOfPeriodPerPeriod,
        "BeforePeriod" : P3BPeriod,
        "BeforeDistance" : P3BDistance,
        "AfterPeriod" : P3APeriod,
        "AfterDistance" : P3ADistance
        }

    PulsarFour = {
        "FractionOfPeriodPerPeriod" : P4FractionOfPeriodPerPeriod,
        "BeforePeriod" : P4BPeriod,
        "BeforeDistance" : P4BDistance,
        "AfterPeriod" : P4APeriod,
        "AfterDistance" : P4ADistance
        }

    PulsarFive = {
        "FractionOfPeriodPerPeriod" : P5FractionOfPeriodPerPeriod,
        "BeforePeriod" : P5BPeriod,
        "BeforeDistance" : P5BDistance,
        "AfterPeriod" : P5APeriod,
        "AfterDistance" : P5ADistance,
        }

    PulsarSix = {
        "FractionOfPeriodPerPeriod" : P6FractionOfPeriodPerPeriod,
        "BeforePeriod" : P6BPeriod,
        "BeforeDistance" : P6BDistance,
        "AfterPeriod" : P6APeriod,
        "AfterDistance" : P6ADistance
        }

    PulsarList = [PulsarOne, PulsarTwo, PulsarThree, PulsarFour, PulsarFive, PulsarSix]
    for Pulsar in PulsarList:
        AccumulatedLength = Pulsar["BeforePeriod"] * 299792458.0
        WorkingPeriod = Pulsar["BeforePeriod"]
        while AccumulatedLength < Pulsar["BeforeDistance"]:
            WorkingPeriod += (WorkingPeriod * Pulsar["FractionOfPeriodPerPeriod"])
            AccumulatedLength += (WorkingPeriod * 299792458.0)
        Pulsar["ReferenceBeforePeriod"] = WorkingPeriod
        AccumulatedLength = Pulsar["AfterPeriod"] * 299792458.0
        WorkingPeriod = Pulsar["AfterPeriod"]
        while AccumulatedLength < Pulsar["AfterDistance"]:
            WorkingPeriod += (WorkingPeriod * Pulsar["FractionOfPeriodPerPeriod"])
            AccumulatedLength += (WorkingPeriod * 299792458.0)
        Pulsar["ReferenceAfterPeriod"] = WorkingPeriod
    for Pulsar in PulsarList:
        if Pulsar["ReferenceAfterPeriod"] > Pulsar["ReferenceBeforePeriod"]:
            LongerPeriod = Pulsar["ReferenceAfterPeriod"]
            ShorterPeriod = Pulsar["ReferenceBeforePeriod"]
        elif Pulsar["ReferenceAfterPeriod"] < Pulsar["ReferenceBeforePeriod"]:
            LongerPeriod = Pulsar["ReferenceBeforePeriod"]
            ShorterPeriod = Pulsar["ReferenceAfterPeriod"]
        WorkingPeriod = ShorterPeriod
        Time = 0
        while WorkingPeriod < LongerPeriod:
            WorkingPeriod += (WorkingPeriod * Pulsar["FractionOfPeriodPerPeriod"])
            Time += WorkingPeriod
        Pulsar["Time"] = Time
    SumOfTimes = 0
    for Pulsar in PulsarList:
        SumOfTimes += Pulsar["Time"]
    AveragedTimeOfTravel = SumOfTimes / len(PulsarList)
    return AveragedTimeOfTravel
