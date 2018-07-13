import os

# Traverses artist and album directories.
class FLACMover:

  def __init__(self):
    pass

  def traverse(self, mp3_root_dir, flac_root_dir):
    """
    """
    dirParser = DirParser()
    folders_to_ignore = ['[Live Mixes]', '[Other]', '[Spoken Word]', '__Eval', '__New (must have tags)', '_Einzelne', '_Various Artists']
    root_dir = 'C:/Users/mathaeus/Music/_SKA'
    dict = dirParser.traverse(mp3_root_dir, folders_to_ignore)

    va_dir = os.path.join(mp3_root_dir, '_Various Artists')
    dict['_Various Artists'] = os.listdir(va_dir)

    artists = dict.keys()
    for artist in artists:
      for album in dict[artist]:
        mp3_dir = os.path.join(mp3_root_dir, artist, album)
        flac_dir = os.path.join(flac_root_dir, artist, album)
        if os.path.exists(flac_dir):
          print("exists: " + flac_dir)
