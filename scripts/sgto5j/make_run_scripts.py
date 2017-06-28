####################################################################
# Type: SCRIPT                                                     #
#                                                                  #
# Description: [description]                                       #
####################################################################

# IMPORTS:
# :IMPORTS

# CLASSES:
# :CLASSES

# VARIABLES:
gmasses = [100, 150, 175, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
hmass_ratio = 0.6
# :VARIABLES

# FUNCTIONS:
def make_new_script(f_in, args, f_out):
	with open(f_in) as fin:
		text = fin.read()
	for key, value in args.items():
		text = text.replace("%%{}%%".format(key.upper()), str(value))
	with open(f_out, "w") as fout:
		fout.write(text)

def main():
	for gmass in gmasses:
		for htcut in [0, 700]:
			name = "sg{}to5j_cutht{}_1step_run.mg5".format(gmass, htcut)
			make_new_script(
				"sgto5j_1step_run.template",
				{
					"gmass": gmass,
					"hmass": int(gmass*hmass_ratio),
					"htcut": htcut,
				},
				name
			)
	return True
# :FUNCTIONS

# MAIN:
if __name__ == "__main__":
	main()
# :MAIN

