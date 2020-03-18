import argparse
import trigger

parser = argparse.ArgumentParser()
parser.add_argument( '--force', action='store_true' )
parser.add_argument( '--read', metavar='hdf5_filename', type=str )
parser.add_argument( '--conv', metavar='data_filename', type=str )
args = parser.parse_args()

# -----------------------------------------
if args.read:
    df = trigger.read_hdf5( args.read )
elif args.conv:
    df = trigger.conv_hdf5( args.conv, args.force )
else:
    parser.print_usage()
    exit()

if df.size == 0:
    exit()

# -----------------------------------------
print( df['UtcTime'] )
