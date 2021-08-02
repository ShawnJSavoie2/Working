# Python 3.9.0

# FractionOfPeriodPerPeriod

def FractionOfPeriodPerPeriod(PeriodAtBeginningOfDay, PeriodAtEndingOfDay, Frequency,
                              FractionOfPeriodPerDay):

    '''

    '''

    PeriodsInDay = Frequency * 86,400
    WorkingFractionOfPeriodPerPeriod = FractionOfPeriodPerDay / PeriodsInDay
    if WorkingFractionOfPeriodPerPeriod / WorkingFractionOfPeriodPerPeriod == 1.0:
        Quantity = 1.0
    else:
        Point = WorkingFractionOfPeriodPerPeriod.index('.')
        Fraction = WorkingFractionOfPeriodPerPeriod[Point:]
        Quantity = 1 / (len(Fraction) ** 10)
    AddOrSubtract = 'Subtract'
    GoodToGo = 'No'
    while GoodToGo == 'No':
        WorkingPeriod = PeriodAtBeginningOfDay
        for I in range(PeriodsInDay):
            WorkingPeriod += (WorkingPeriod * WorkingFractionOfPeriodPerPeriod)
        if WorkingPeriod < PeriodAtEndingOfDay:
            if AddOrSubtract == 'Add':
                WorkingFractionOfPeriodPerPeriod += Quantity
            else:
                AddOrSubtract = 'Add'
                Quantity /= 10
                WorkingFractionOfPeriodPerPeriod += Quantity
        elif WorkingPeriod > PeriodAtEndingOfDay:
            if AddOrSubtract == 'Subtract':
                WorkingFractionOfPeriodPerPeriod += Quantity
            else:
                AddOrSubtract = 'Subtract'
                Quantity /= 10
                WorkingFractionOfPeriodPerPeriod += Quantity
        else:
            GoodToGo = 'Yes'
    FractionOfPeriodPerPeriod = WorkingFractionOfPeriodPerPeriod
    return FractionOfPeriodPerPeriod
