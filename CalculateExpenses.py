import numpy as np

AshutoshPaysFood = 82.00
AshutoshPaysFirstRound = 120.51
DeepsingPaysSecondRound = 75.96

#TipFactor = 82.00/74.84


TipFactor = 82.00/69.94

print("The Tip Factor is: ", round(TipFactor,2))

PragyaPays = 9.99*TipFactor+(AshutoshPaysFirstRound+DeepsingPaysSecondRound)/6.0
MarianaPays  =  (8.99+6.99)*TipFactor+(AshutoshPaysFirstRound+DeepsingPaysSecondRound)/6.0
PrajwalPays  =  1./8.*(15.99)*TipFactor+(AshutoshPaysFirstRound+DeepsingPaysSecondRound)/6.0
DeepsingPays  =  7./8.*(15.99)*TipFactor+(AshutoshPaysFirstRound+DeepsingPaysSecondRound)/6.0
BjoernPays  =  (27.98)/2.*TipFactor+(AshutoshPaysFirstRound+DeepsingPaysSecondRound)/6.0
AshutoshPays  =  (27.98)/2.*TipFactor+(AshutoshPaysFirstRound+DeepsingPaysSecondRound)/6.0

print("Prajwal Pays: ",round(PrajwalPays,2))
print("Prajwal Pays: 26.81 to Deepsing.")
print("Prajwal Pays: ",round(PrajwalPays-26.81,2), "to Ashutosh")
print("Mariana Pays: ", round(MarianaPays, 2), " to Ashutosh")
print("Pragya Pays: ", round(PragyaPays, 2), " to Ashutosh")
print("Bjoern Pays: ", round(BjoernPays, 2), " to Ashutosh")
print("Ashutosh Gets: ", -round(AshutoshPays-AshutoshPaysFood-AshutoshPaysFirstRound, 2))
print("Deepsing Gets: ", round(DeepsingPays- DeepsingPaysSecondRound,2))

print("Total Expense: ", PrajwalPays+MarianaPays+PragyaPays+BjoernPays+AshutoshPays+DeepsingPays)
print("Total Credit: ", AshutoshPaysFood+AshutoshPaysFirstRound+DeepsingPaysSecondRound)