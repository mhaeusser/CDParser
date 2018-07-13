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
          self.move_flac(mp3_dir, flac_dir)
        else:
          print("mp3 only: " + mp3_dir)

  def move_flac(self, mp3_dir, flac_dir):
    new_mp3_dir = os.path.join(mp3_dir, 'mp3')
    new_flac_dir = os.path.join(mp3_dir, 'flac')
    # mkdir new_mp3_dir
    # mkdir new_flac_dir
    print('move all files from ' + mp3_dir + ' into ' + new_mp3_dir)
    print('move all files from ' + flac_dir + ' into ' + new_flac_dir)
