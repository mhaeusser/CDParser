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
          dict[artist_dir] = album_folders
        else:
          print('please check ' + artist_dir)
    return dict

  def format_dict(self, dict):
    """
    pretty-prints dict
    """
    text = ''
    keys = dict.keys()
    for key in keys:
      for elem in dict[key]:
        text += key + "   ->   " + elem + "\n"
    return text
