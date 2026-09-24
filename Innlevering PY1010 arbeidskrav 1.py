"""
Innlevering arbeidskrav 1 PY1010
Siree S. Sæther 2026 09
"""



km = 10000      #Km kjørt i gjennomsnitt per år
år = 1      
fe = 5000     #Kroner forsikring elbil per år
fb = 7500    #Kroner forsikring bensinbil per år
tfa = 8.38   #Kroner trafikkforsikringsvgift per dag

kmpe = (0.2 * km)*2     #Kilometerpris i kr for elbil (0.2 kwh/km * km)*2 kr
kmpb = 1 * km       #Kilometerpris i kr for bensinbil, 1 kr * km
bae = 0.1 * km      #Bomavgift for elbil. 0.1kr * km
bab = 0.3 * km      #Bomavgift bensinbil


#%% Pris bensinbil
    
årspris_bensin = (fb * år) + (tfa * 365) + kmpb + bab       #Summering utgifter bensin

#%% Pris elbil

årspris_elbil = (fe * år) + (tfa * 365) + kmpe + bae        #Summering utgifter elbil



#%% Presentasjon

differanse = abs(årspris_bensin-årspris_elbil)      #Differansen mellom årskostnadene, som positiv verdi

print('\nTotalkostnaden for en elbil som har kjørt',km, 'km er', årspris_elbil, \
      'kr og totalkostnaden for en bensinbil som har kjørt samme distanse er', \
          årspris_bensin, 'kr.\n\nDifferansen er altså', differanse, 'kr.')
