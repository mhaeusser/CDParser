class TraverserRunner:

  # Runs Traverser with path hard-coded here.
  if __name__ == "__main__":
    dirParser = DirParser()
    #traverser.traverse('D:/SkaMP3', 'C:/temp/CDs.csv')
    folders_to_ignore = ['[Live Mixes]', '[Other]', '[Spoken Word]', '__Eval', '__New (must have tags)', '_Einzelne', '_Various Artists']
    dict = dirParser.traverse('C:/Users/mathaeus/Music/_SKA', folders_to_ignore)

    print(dict)
