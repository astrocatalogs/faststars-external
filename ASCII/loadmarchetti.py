from astropy.io.ascii import read

data = read("./marchetti,txt", format='fixed_width')
for row in pbar(data, task_str):
    oname = 'SDSS'+str(row['SDSS'])
