import os

class DirParserRunner:

  # Runs DirParser with path hard-coded here.
  if __name__ == "__main__":
    dirParser = DirParser()
    folders_to_ignore = ['___FLAC', '[Live Mixes]', '[Other]', '[Spoken Word]', '__Eval', '__New (must have tags)', '_Einzelne', '_Various Artists']
    #root_dir = 'C:/Users/mathaeus/Music/_SKA'
    root_dir = 'D:/SkaMP3'
    dict = dirParser.traverse(root_dir, folders_to_ignore)

    va_dir = os.path.join(root_dir, '_Various Artists')
    dict['_Various Artists'] = os.listdir(va_dir)

    text = dirParser.format_dict(dict)
    print(text)
    out_file = open("C:/temp/album_dirs.txt", "w", encoding="utf8")
    out_file.write(text)
