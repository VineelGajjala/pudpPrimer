s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port)) # server needs binding, but client doesn't