import os

# Traverses artist and album directories.
class DirParser:

  def __init__(self):
    pass

  def traverse(self, root_dir, dirs_to_ignore):
    """
    traverses root_dir, considers all contained folders as artist folders
    writes results into file
    """
    print('Starting.')

    dict = {} # maps artist dir (absolute) to list of contained folders
    artist_dirs = os.listdir(root_dir)

    for artist_dir in artist_dirs:
      # ignore special folders
      if not artist_dir in dirs_to_ignore:
        abs_artist_dir = os.path.join(root_dir, artist_dir)
        if (os.path.isdir(abs_artist_dir)):
          # get list of contained folders, add them
          album_folders = os.listdir(abs_artist_dir)
          dict[abs_artist_dir] = album_folders
        else:
          print('please check ' + artist_dir)
    return dict

  def print_artist_folder(self, artist_dir, artist_name, out_file):
    """
    inside artist_dir, lists all folders
    (which must contain albums except for the [Info] folder)
    """
    album_folders = os.listdir(artist_dir)
    for album_folder in album_folders:
      if album_folder != '[Info]':
        out_file.write(artist_name + "\t" + album_folder + "\n")
