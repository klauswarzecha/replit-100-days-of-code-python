import csv
import os


def normalize(data: str, char: str = '_') -> str:
  """Replace all blanks by another char"""
  return char.join(data.split())

songs = '100MostStreamedSongs.csv'

# create a single basedir for all artists
# this is easier to remove
basedir = 'music'
try:
  os.mkdir(basedir)
except FileExistsError:
  pass

with open(songs, 'r') as file:
  stream = csv.DictReader(file)
  header = next(stream)
  for song in stream:
    dirname = normalize(song.get('Artist(s)'))
    dirpath = '/'.join((basedir, dirname))
    # create directory if it does not exist
    try:
      os.mkdir(dirpath)
    except FileExistsError:
      pass
    fname = normalize(song.get('Song'))
    filepath = '/'.join((dirpath, fname))
    # create empty text file
    with open(filepath, 'w'):
      pass
