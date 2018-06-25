import os

# Traverses artist and album directories.
class Traverser:
    
  def __init__(self):
    pass

  def traverse(self, root_dir):
    print('Starting.')

    artist_dirs = os.listdir(root_dir)
    for artist_dir in artist_dirs:
      self.print_artist_folder(root_dir, artist_dir)

  def print_artist_folder(self, root_dir, artist_dir):
    folder = os.path.join(root_dir, artist_dir)
    album_folders = os.listdir(folder)
    print(artist_dir)
    for album_folder in album_folders:
      print("\t\t" + album_folder)
