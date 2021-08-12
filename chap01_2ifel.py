print(" *** Wind classification ***")
speed = float(input('Enter wind speed (km/h) : '))

if speed    >= 209  : print("Wind classification is Super Typhoon.")
elif speed  >= 102  : print("Wind classification is Typhoon.")
elif speed  >= 56   : print("Wind classification is Tropical Storm.")
elif speed  >= 52   : print("Wind classification is Depression.")
elif speed  >= 0    : print("Wind classification is Breeze.")

