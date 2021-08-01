# Python 3.9.0

# AveragedTimeOfTravel

def AveragedTimeOfTravel(
    
    P1FractionOfPeriodPerPeriod,
    P1BPeriod,
    P1BDistance,
    P1BWavelength
    P1APeriod,
    P1ADistance,
    P1AWavelength,
    
    P2FractionOfPeriodPerPeriod,
    P2BPeriod,
    P2BDistance,
    P2BWavelength
    P2APeriod,
    P2ADistance,
    P2AWavelength,

    P3FractionOfPeriodPerPeriod,
    P3BPeriod,
    P3BDistance,
    P3BWavelength
    P3APeriod,
    P3ADistance,
    P3AWavelength,

    P4FractionOfPeriodPerPeriod,
    P4BPeriod,
    P4BDistance,
    P4BWavelength
    P4APeriod,
    P4ADistance,
    P4AWavelength,

    P5FractionOfPeriodPerPeriod,
    P5BPeriod,
    P5BDistance,
    P5BWavelength
    P5APeriod,
    P5ADistance,
    P5AWavelength,

    P6FractionOfPeriodPerPeriod,
    P6BPeriod,
    P6BDistance,
    P6BWavelength
    P6APeriod,
    P6ADistance,
    P6AWavelength
    
    ):

    '''

    '''

    PulsarOne = {
        FractionOfPeriodPerPeriod = P1FractionOfPeriodPerPeriod,
        BeforePeriod = P1BPeriod,
        BeforeDistance = P1BDistance,
        BeforeWavelength = P1BWavelength,
        AfterPeriod = P1APeriod,
        AfterDistance = P1ADistance,
        AfterWavelength = P1AWavelength
        }

    PulsarTwo = {
        FractionOfPeriodPerPeriod = P2FractionOfPeriodPerPeriod,
        BeforePeriod = P2BPeriod,
        BeforeDistance = P2BDistance,
        BeforeWavelength = P2BWavelength,
        AfterPeriod = P2APeriod,
        AfterDistance = P2ADistance,
        AfterWavelength = P2AWavelength
        }

    PulsarThree = {
        FractionOfPeriodPerPeriod = P3FractionOfPeriodPerPeriod,
        BeforePeriod = P3BPeriod,
        BeforeDistance = P3BDistance,
        BeforeWavelength = P3BWavelength,
        AfterPeriod = P3APeriod,
        AfterDistance = P3ADistance,
        AfterWavelength = P3AWavelength
        }

    PulsarFour = {
        FractionOfPeriodPerPeriod = P4FractionOfPeriodPerPeriod,
        BeforePeriod = P4BPeriod,
        BeforeDistance = P4BDistance,
        BeforeWavelength = P4BWavelength,
        AfterPeriod = P4APeriod,
        AfterDistance = P4ADistance,
        AfterWavelength = P4AWavelength
        }

    PulsarFive = {
        FractionOfPeriodPerPeriod = P5FractionOfPeriodPerPeriod,
        BeforePeriod = P5BPeriod,
        BeforeDistance = P5BDistance,
        BeforeWavelength = P5BWavelength,
        AfterPeriod = P5APeriod,
        AfterDistance = P5ADistance,
        AfterWavelength = P5AWavelength
        }

    PulsarSix = {
        FractionOfPeriodPerPeriod = P6FractionOfPeriodPerPeriod,
        BeforePeriod = P6BPeriod,
        BeforeDistance = P6BDistance,
        BeforeWavelength = P6BWavelength,
        AfterPeriod = P6APeriod,
        AfterDistance = P6ADistance,
        AfterWavelength = P6AWavelength
        }

    PulsarList = [PulsarOne, PulsarTwo, PulsarThree, PulsarFour, PulsarFive, PulsarSix]
    for Pulsar in PulsarList:
        AccumulatedLength = Pulsar[BeforeWavelength]
        WorkingPeriod = Pulsar[BeforePeriod]
        while AccumulatedLength < Pulsar[BeforeDistance]:
            WorkingPeriod += WorkingPeriod * Pulsar[FractionOfPeriodPerPeriod]
            AccumulatedLength += WorkingPeriod * c
        Pulsar[ReferenceBeforePeriod] = WorkingPeriod
        AccumulatedLength = Pulsar[AfterWavelength]
        WorkingPeriod = Pulsar[AfterPeriod]
        while AccumulatedLength < Pulsar[AfterDistance]:
            WorkingPeriod += WorkingPeriod * Pulsar[FractionOfPeriodPerPeriod]
            AccumulatedLength += WorkingPeriod * c
        Pulsar[ReferenceAfterPeriod] = WorkingPeriod
    for Pulsar in PulsarList:
        if Pulsar[ReferenceAfterPeriod] > Pulsar[ReferenceBeforePeriod]:
            LongerPeriod = Pulsar[ReferenceAfterPeriod]
            ShorterPeriod = Pulsar[ReferenceBeforePeriod]
        elif Pulsar[ReferenceAfterPeriod] < Pulsar[ReferenceBeforePeriod]:
            LongerPeriod = Pulsar[ReferenceBeforePeriod]
            ShorterPeriod = Pulsar[ReferenceAfterPeriod]
        WorkingPeriod = ShorterPeriod
        Time = 0
        while WorkingPeriod < LongerPeriod:
            WorkingPeriod += WorkingPeriod * Pulsar[FractionOfPeriodPerPeriod]
            Time += WorkingPeriod
        Pulsar[Time] = Time
    SumOfTimes = 0
    for Pulsar in PulsarList:
        SumOfTimes += Pulsar[Time]
    AveragedTimeOfTravel = SumOfTimes / len(PulsarList)
    return AveragedTimeOfTravel
    
    
