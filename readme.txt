Snake Reader is Optical Character Recognition program fully written in Python by students of Wroc³aw University of Technology (Computer Science). Program uses neural network in recognition stage and optional dictionary checking later. It has it's own GUI but can also be used by a command line (as a plugin).



An interaction with a program using a command line:

> SnakeReader.py [input file] [output file] [options]

[input file] a path to a .jpg or .bmp file, which will be recognized
[output file] a place and file name, where the outcome text will be saved
[options]:
	-d (dictionary) option telling that program should use dictionary from cd (cd) or from internet server (server)
	-s (size) font size from a scan
	-r (resolution) scan resolution
	-q (quality) scan quality (poor or ok)
	-rq (recognition quality) quality of recognition (good or poor)
	-p (parameters) file with parameters

Example:
C:\Documents and Settings\User\Pulpit>SnakeReader.py Scan.jpg Text.txt -d cd -s 12 -r 300 -q ok -rq good -p parameters.bin