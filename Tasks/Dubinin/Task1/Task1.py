#Initial Data
Amount = 20000
Year = 5
IR_y = 0.15
#Solution
Month = 12 * Year
IR_m = IR_y / 12
Amount = Amount * (1+IR_m)**(Month)
print(round(Amount, 2))
