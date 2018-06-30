import os

# Traverses artist and album directories.
class Traverser:
    
  def __init__(self):
    pass

  def traverse(self, root_dir, out_filename):
    """
    traverses root_dir, considers all contained folders as artist folders
    writes results into file
    """    
    print('Starting.')
    out_file = open(out_filename, "w", encoding="utf8")

    special_folders = self.get_special_folders()

    artist_dirs = os.listdir(root_dir)

    # "regular" folders
    for folder in artist_dirs:
      # ignore special folders
      if not folder in special_folders:      
        artist_dir = os.path.join(root_dir, folder)
        if (os.path.isdir(artist_dir)):
          self.print_artist_folder(artist_dir, folder, out_file)

    # "_Various Artist"
    various_artists_dir = os.path.join(root_dir, '_Various Artists')
    self.print_artist_folder(various_artists_dir, 'Various Artists', out_file)

    print('See ' + out_filename)

  def print_artist_folder(self, artist_dir, artist_name, out_file):
    """
    inside artist_dir, lists all folders
    (which must contain albums except for the [Info] folder)
    """
    album_folders = os.listdir(artist_dir)
    for album_folder in album_folders:
      if album_folder != '[Info]':
        out_file.write(artist_name + "\t" + album_folder + "\n")

  def get_special_folders(self):
    """reserved folder names"""
    return ['[Live Mixes]', '[Other]', '[Spoken Word]', '__Eval', '__New (must have tags)', '_Einzelne', '_Various Artists']
