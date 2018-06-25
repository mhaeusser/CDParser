import os

# Traverses artist and album directories.
class Traverser:
    
  def __init__(self):
    pass

  def traverse(self, root_dir):
    print('Starting.')
    special_folders = self.get_special_folders()

    artist_dirs = os.listdir(root_dir)
    for folder in artist_dirs:
      
      if not folder in special_folders:
      
        artist_dir = os.path.join(root_dir, folder)
        if (os.path.isdir(artist_dir)):
          self.print_artist_folder(root_dir, artist_dir)

  def print_artist_folder(self, root_dir, artist_dir):
    album_folders = os.listdir(artist_dir)
    print(artist_dir)
    for album_folder in album_folders:
      print("\t\t" + album_folder)

  def get_special_folders(self):
    return ['[Live Mixes]', '[Other]', '[Spoken Word]', '__Eval', '__New (must have tags)', '_Einzelne', '_Various Artists']
