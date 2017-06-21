if [ -z "$1" ]; then
	echo "[ERROR] You need to provide the path to your MadGraph area as the argument to this script."
	exit 1
fi

cp cards/* $1/cards &&
cp scripts/* $1/scripts &&
rm -rf $1/models/RPVMSSM_UFO &&
cp -r RPVMSSM_UFO $1/models
