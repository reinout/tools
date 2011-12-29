#!/usr/bin/env python

from string import split,join
def dos2unix(data):
	return join(split(data,'\r\n'),'\n')

def unix2dos(data):
	return join(split(dos2unix(data),'\n'),'\r\n')
def confirm(file):
	s=raw_input('%s? ' %file)
	return s and s[0]=='y'
def usage():
	import sys
	print """\
USAGE
    dos2unix.py [-iuvnfcd] [-b extension] file {file}
DESCRIPTION
    Converts files from unix to dos and reverse. It keeps the
    mode of the file.
    Binary files are not converted unless -f is specified.
OPTIONS
    -i      interactive (ask for each file)
    -u      unix2dos (inverse functionality)
    -v      print files that are converted
    -n      show but don't execute (dry mode)
    -f      force. Even if the file is not ascii convert it.
    -b ext  use 'ext' as backup extension (default .bak)
    -c      don't make a backup
    -d      keep modification date and mode
"""
	sys.exit()

def main():
	import sys,re,os,shutil,getopt
	try:
		opts,args=getopt.getopt(sys.argv[1:],"fniuvdc")
		args[0]
	except:
		usage()
	force=0
	noaction=0
	convert=dos2unix
	verbose=0
	copystat=shutil.copymode
	backup='.bak'
	nobackup=0
	interactive=0
	for k,v in opts:
		if k=='-f':
			force=1
		elif k=='-n':
			noaction=1
			verbose=1
		elif k=='-i':
			interactive=1
		elif k=='-u':
			convert=unix2dos
		elif k=='-v':
			verbose=1
		elif k=='-b':
			backup=v
		elif k=='-d':
			copystat=shutil.copystat
		elif k=='-c':
			nobackup=1
	asciiregex=re.compile('[ -~\r\n\t\f]+')
	for file in args:
		if not os.path.isfile(file) or file[-len(backup):]==backup:
			continue
		fp=open(file)
		head=fp.read(10000)
		if force or len(head)==asciiregex.match(head):
			data=head+fp.read()
			#newdata=unix2dos(data)
			newdata=convert(data)
			if newdata!=data:
				if verbose and not interactive:
					print file
				if not interactive or confirm(file):
					if not noaction:
						newfile=file+'.@'
						f=open(newfile,'w')
						f.write(newdata)
						f.close()
						copystat(file,newfile)
						if backup:
							backfile=file+backup
							os.rename(file,backfile)
						else:
							os.unlink(file)
						os.rename(newfile,file)
						if nobackup:
							os.unlink(backfile)

try:
	main()
except KeyboardInterrupt:
	pass
