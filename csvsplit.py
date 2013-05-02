import csv
import argparse

def split(infile,field, dest=''):
  fp = open(infile,'rb')
	topline = fp.readlines()[0]
	names = topline.split(',')

	i = 0
	for x in range(0,len(names)):
		i = x
		if names[i].lower() == 'team':
			#i has been set to the correct position
			break
	
	fp.seek(0)

	outfiles = {}
	csvwriters = {}

	if dest != '' and not dest.endswith('/'):
		dest = dest + '/'

	rx = csv.reader(fp)
	#cast off first line
	rx.next()

	for row in rx:
		if row[i] not in outfiles:
			outfiles[row[i]] = open(dest + row[i]+'.csv','wb')
			csvwriters[row[i]] = csv.writer(outfiles[row[i]])

			csvwriters[row[i]].writerow(topline.split(','))

		csvwriters[row[i]].writerow(row)

	for of in outfiles.keys():
		outfiles[of].close()

	fp.close()

def main():
	parser = argparse.ArgumentParser(description='Take one csv file and divide into multiple files based on a particular field')
	parser.add_argument('--infile',dest='infile',help='Source CSV file',required=True)
	parser.add_argument('--field',dest='field',help='Field to divide on',required=True)
	parser.add_argument('--dest',dest='dest',help='Optional dir to store CSV files in')
	args = parser.parse_args()

	if args.dest:
		split(args.infile,args.field,dest=args.dest)
	else:
		split(args.infile,args.field)

if __name__ == '__main__':
	main()
