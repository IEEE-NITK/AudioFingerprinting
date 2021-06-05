
#Parameters for making spectrograms
FRAME_SIZE=2048
HOP_SIZE=512

#Parameters for finding peaks
peak_neighborhood_size = 15
min_amp = 15   #Amplitude value for the filter
size = (peak_neighborhood_size*2) +1

#Parameters for getting hashes
min_time_delta = 0
max_time_delta = 300
range_frequencies = 1000
fan_value = 20

#Parameters for recording a song from microphone
sampling_rate = 44100    #Sampling frequency
duration = 10    #Recording duration
