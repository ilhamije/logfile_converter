import argparse

"""
1. Convert *.log to json and text
2. Contoh penggunaan:
    - Mengkonversi menjadi file json
    $ mytools /var/log/nginx/error.log -t json
    - Mengkonversi menjadi file text
    $ mytools /var/log/nginx/error.log -t text
3. Default output is 'text'
    mytools /var/log/nginx/error.log --> error.txt
4. User juga bisa memilih dimana dia akan meletakan file output tersebut.
    Dengan menggunakan flag -o.
    $ mytools /var/log/nginx/error.log -o /User/johnmayer/Desktop/nginxlog.txt
    $ mytools /var/log/nginx/error.log -t json -o /User/johnmayer/Desktop/nginxlog.json
5. Help
    Tools tersebut juga harus memiliki flag -h yang berfungsi menampilkan petunjuk penggunaanya.
    $ mytools -h

"""
def main(args):
    args_dict = vars(args)
    print(args_dict)
    print('filename is: ', args_dict['file'])
    print(target_ext(args_dict['target']))
    print(output_dir(args_dict['output']))


def target_ext(extname):
    """
    Convert file using selected format.
    Use *.txt format as default.
    """
    if extname:
        return 'convert selected format'
    else:
        return 'convert into .txt'


def output_dir(todir):
    """
    Define output directory.
    Use current directory as default.
    """
    if todir:
        res = """
        check if directory exist
        if not, create dir
        copy file into dir
        """
        return res
    else:
        res = """
        use current directory of run.py
        copy file to
        """
        return res

def file_check(opener):
    def ext_check(filename):
        if not filename.lower().endswith('log'):
            raise ValueError('*.log file only')
        return opener(filename)
    return ext_check


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('file',
                    type=file_check(argparse.FileType(mode="w")),
                    help='*.log file only')
    p.add_argument('-t', '--target',
                    help='-t <json|text>',
                    choices=['text', 'json'])
    p.add_argument('-o', '--output',
                    help='-o <path/to/output/file>',
                    type=argparse.FileType(mode="w"))
    args = p.parse_args()

    main(args)

    # with args.file.open('r') as file:
    #     print(file.read())
