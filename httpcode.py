from httpz import HTTPStatusCodes
from make_colors import make_colors
from textwrap import wrap
import argparse
import sys

def get_code(code, desc = False):
    for i in HTTPStatusCodes.get_all():
        if code:
            if desc:
                if code.lower() in i.message.lower() or code.lower() in str(i.code).lower():
                    print(
                        make_colors(str(i.code), 'b', 'lg') + ": " + \
                        make_colors(i.message, 'lw', 'm') + " || " + \
                        make_colors(i.description, 'b', 'y')
                    )
                else:
                    print(
                        make_colors(str(i.code), 'lc') + ": " + \
                        make_colors(i.message, 'ly') + " || " + \
                        make_colors(i.description, 'lg')
                    )                           
                    
            else:
                if code.lower() in i.message.lower() or code.lower() in str(i.code).lower():
                    print(
                        make_colors(str(i.code), 'b', 'lg') + ": " + \
                        make_colors(i.message, 'lw', 'm')
                    )
                else:
                    print(
                        make_colors(str(i.code), 'lc') + ": " + \
                        make_colors(i.message, 'ly')
                    )
        else:
            if desc:
                print(
                    make_colors(str(i.code), 'lc') + ": " + \
                    make_colors(i.message, 'ly') + " || " + \
                    make_colors(i.description, 'lg')
                )                           
                    
            else:
                print(
                    make_colors(str(i.code), 'lc') + ": " + \
                    make_colors(i.message, 'ly')
                )            
    
    print("\n")
    print(make_colors("Created by:", 'lw', 'bl') + " " + make_colors("Hadi Cahyadi", 'lw', 'r'))

def usage():
    parser = argparse.ArgumentParser()
    if len(sys.argv) > 1:
        if sys.argv[1][0] == '-':
            parser.add_argument('-c', '--code', help = 'Code or Message', action = 'store')
            parser.add_argument('-d', '--description', help = 'Show with description too !', action = 'store_true')
            
            args = parser.parse_args()
            get_code(args.code, args.description) 
        else:
            parser.add_argument('CODE', help = 'Code or Message', action = 'store')
            parser.add_argument('-d', '--description', help = 'Show with description too !', action = 'store_true')
            
            args = parser.parse_args()
            get_code(args.CODE, args.description)
    else:
        parser.add_argument('-c', '--code', help = 'Code or Message', action = 'store')
        parser.add_argument('-d', '--description', help = 'Show with description too !', action = 'store_true')        
        parser.print_help()
        
        args = parser.parse_args()
        
        get_code(args.code, args.description)

if __name__ == '__main__':
    usage()