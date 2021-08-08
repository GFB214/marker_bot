import argparse,os

input_path = "/root/olddriver/marker/input"
output_path = "/root/olddriver/marker/output"
watermark = "广州修车大队\n@OLDDRIVERGZ"

TTF_FONT = u'./font/WenQuanYiMicroHei.ttf'
# TTF_FONT = os.path.join("font", "WenQuanYiMicroHei.ttf")
# TTF_FONT = os.path.join(os.path.dirname(os.path.abspath(__fpython marile__)), TTF_FONT)

def init():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t","--token",help="telegram bot token")
    parse.add_argument("-i", "--input", default=input_path,
                help="image input directory, default is ./input")
    parse.add_argument("-m", "--mark", default=watermark, 
                    type=str, help="watermark content")
    parse.add_argument("-o", "--out", default=output_path,
                    help="image output directory, default is ./output")
    parse.add_argument("-c", "--color", default="#000000", type=str,
                    help="text color like '#000000', default is #8B8B1B")
    parse.add_argument("-s", "--space", default=75, type=int,
                    help="space between watermarks, default is 75")
    parse.add_argument("-a", "--angle", default=30, type=int,
                    help="rotate angle of watermarks, default is 30")
    parse.add_argument("--size", default=40, type=int,
                    help="font size of text, default is 50")
    parse.add_argument("--opacity", default=0.1, type=float,
                    help="opacity of watermarks, default is 0.15")
    parse.add_argument("--quality", default=80, type=int,
                    help="quality of output images, default is 90")
    parse.add_argument("--font", default=TTF_FONT, type=str,
                    help="font file, absolute path")
    args = parse.parse_args()
    if args.token == None :
        print("need bot token!!!!!")
        exit()
    return args


