
#!/usr/bin/env python3

import os

input_file = "nsd.txt"
output_dir = "./op/"

pattern = 'nfvo:nfvo nsd'
count=0

with open(input_file, 'r') as input_file:
    input_data = input_file.readline()
    output_file = None

    while input_data:
        if input_data.startswith(pattern):
            if output_file :
                output_file.close()
            count=count+1;
            # Create new output file name
            output_filename = str(count)+".txt"
            output_path = os.path.join(output_dir, output_filename)
            # open the output file
            output_file = open(output_path,'w')
            output_file.write(input_data)
        elif output_file:
            output_file.write(input_data)    
        input_data = input_file.readline()
    if output_file :
        output_file.close()     