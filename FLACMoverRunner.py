class TraverserRunner:

  # Runs Traverser with path hard-coded here.
  if __name__ == "__main__":
    flacMover = FLACMover()
    mp3_root_dir = 'D:/SkaMP3'
    flac_root_dir = 'D:/SkaMP3/___FLAC'
    flacMover.traverse(mp3_root_dir, flac_root_dir)
