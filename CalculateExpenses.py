AshutoshPaidFood = 82.00
MariannaPaidFirstRound = 120.51
DeepsingPaidSecondRound = 75.96

#TipFactor = 82.00/74.84


TipFactor = 82.00/69.94

print("The Tip Factor is: ", round(TipFactor,2))

PragyaPays = 9.99*TipFactor+(MariannaPaidFirstRound+DeepsingPaidSecondRound)/6.0
MarianaPays  =  (8.99+6.99)*TipFactor+(MariannaPaidFirstRound+DeepsingPaidSecondRound)/6.0
PrajwalPays  =  1./8.*(15.99)*TipFactor+(MariannaPaidFirstRound+DeepsingPaidSecondRound)/6.0
DeepsingPays  =  7./8.*(15.99)*TipFactor+(MariannaPaidFirstRound+DeepsingPaidSecondRound)/6.0
BjoernPays  =  (27.98)/2.*TipFactor+(MariannaPaidFirstRound+DeepsingPaidSecondRound)/6.0
AshutoshPays  =  (27.98)/2.*TipFactor+(MariannaPaidFirstRound+DeepsingPaidSecondRound)/6.0

print("Prajwal Pays: ",round(PrajwalPays,2))
print("Prajwal Pays: 26.81 to Deepsing.")
print("Prajwal Pays: ",round(PrajwalPays-26.81,2), "to Ashutosh")
print("*"*5)
print("Marianna  Gets: ", -round(MarianaPays-MariannaPaidFirstRound, 2))
print("49.15 from Bjoern")
print(round(69.03-49.15,2), " from Pragya")
print("*"*5)
print("Pragya Pays: ", round(PragyaPays, 2))
print("Pragya Pays: ", 19.88, "to Marianna" )
print("Pragya Pays: ", round(44.46-19.88,2), "to Ashutosh" )
print("*"*5)
print("Bjoern Pays: ", round(BjoernPays, 2), " to Mariana")
print("*"*5)
print("Ashutosh Gets: ", -round(AshutoshPays-AshutoshPaidFood, 2))
print("24.58 from Pragya")
print("8.28 from Pragya")
print("*"*5)
print("Deepsing Gets: ", -round(DeepsingPays- DeepsingPaidSecondRound,2), " from Prajwal")
print("*"*30)
print("Total Expense: ", round(PrajwalPays+MarianaPays+PragyaPays+BjoernPays+AshutoshPays+DeepsingPays,2))
print("Total Credit: ", round(AshutoshPaidFood+MariannaPaidFirstRound+DeepsingPaidSecondRound,2))
print("*"*30)