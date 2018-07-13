class TraverserRunner:

  # Runs Traverser with path hard-coded here.
  if __name__ == "__main__":
    traverser = Traverser()
    root_dir = 'C:/Users/mathaeus/Music/_SKA'
    #root_dir = 'D:/SkaMP3'
    out_file = 'C:/temp/CDs.csv'
    traverser.traverse(root_dir, out_file)
