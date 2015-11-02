input_file = 'domains.txt'

#read file and create a list with the lines in file
domains_file = open(input_file)
domains = domains_file.readlines()
domains_file.close()


# deletes or creates file (no append)
free_domains = open('free_domains.txt', 'w')

import socket

for domain in domains:
	try:
		#rstrip removes the blank lines at the end!!!
		bla = socket.gethostbyname("www." + domain.rstrip())
		print(bla)
	except socket.gaierror:
		print(socket.gaierror)
		# not getting back an ip, write to file
		free_domains.write(domain)
# close file
free_domains.close()