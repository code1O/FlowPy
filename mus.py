# -*-coding: utf-8 -*-



from synthesizer import Player, Synthesizer, Waveform

class musnotes:
    
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    
    # Definición de la frecuencia 
    # de las notas
    # creando una tupla

    teclas=[
    185.00, # Fa# Solb
    196.00, # Sol
    207.65, # Sol# Lab
    220.00, # La
    233.08, # La# Sib
    246.94, # Si
    261.63, # Do
    277.18, # Do# Reb
    293.66, # Re
    311.13, # Re# Mib
    329.63, # Mi
    349.23, # Fa
    369.99, # Fa# Solb
    392.00, # Sol
    415.30, # Sol# Lab
    440.00, # La
    466.16, # La# Sib
    493.88, # Si
    523.25, # Do
    554.37, # Do# Reb
    587.33, # Re
    622.25, # Re# Mib
    659.26 # Mi 
    ]

    #Definición de las notas conforme 
    # a la posición en la tupla 
    # y su frecuencia

    SOLb = teclas[0]
    SOL = teclas[1]
    LAb = teclas[2]
    LA = teclas[3]
    SIb = teclas[4]
    SI = teclas[5]
    DO2 = teclas[6]
    REb2 = teclas[7]
    RE2 = teclas[8]
    MIb2 = teclas[9]
    MI2 = teclas[10]
    FA2 = teclas[11]
    SOLb2 = teclas[12]
    SOL2 = teclas[13]
    LAb2 = teclas[14]
    LA2 = teclas[15]
    SIb2 = teclas[16]
    SI2 = teclas[17]
    DO3 = teclas[18]
    REb3 = teclas[19]
    RE3 = teclas[20]
    MIb3 = teclas[21]
    MI3 = teclas[22]