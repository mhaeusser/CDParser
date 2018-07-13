class TraverserRunner:

  # Runs DirParser with path hard-coded here.
  if __name__ == "__main__":
    dirParser = DirParser()
    folders_to_ignore = ['[Live Mixes]', '[Other]', '[Spoken Word]', '__Eval', '__New (must have tags)', '_Einzelne', '_Various Artists']
    dict = dirParser.traverse('C:/Users/mathaeus/Music/_SKA', folders_to_ignore)

    text = dirParser.format_dict(dict)
    print(text)
    out_file = open("C:/temp/album_dirs.txt", "w", encoding="utf8")
    out_file.write(text)
