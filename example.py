import olex
import olx
#import sys
from fragmentdb import FragmentTable
from olexFunctions import OlexFunctions
OV = OlexFunctions()
import cProfile
'''
To run this example script, type spy.example("Hello") in Olex2
'''

def example(text="No Text Provided"):
  print "Example Function is now printing your text: %s" %text

OV.registerFunction(example)

def dktest():
  datadir = olex.f("DataDir()")
  basedir = olex.f("BaseDir()")
  print('hello world')
  print(datadir)
  print(basedir)
  print(olx.xf.GetFormula('list'))


OV.registerFunction(dktest)


def olex_functions():
  #print(olx.xf.latt.IsGrown())
  print(help(olx.xf.au.NewAtom))

      

OV.registerFunction(olex_functions)

dbfile = 'F:\Programme\Olex2-1.2-dev\etc\scripts\dk-database.sqlite'
db = FragmentTable(dbfile)

def all_frags():
  print(db.get_all_fragment_names())


def match_dbfrag(fragId=17):
  for i in db.get_fragment(fragId)[1]:
    label = str(i[0])
    print(i[0], i[2],i[3],i[4])
    x, y, z = olx.xf.au.Fractionalise(i[2],i[3],i[4]).split(',')
    id = olx.xf.au.NewAtom(label, x, y, z, False)
    print('adding {}, Id: {}, coords: {} {} {}'.format(i[0], id, x, y, z))
    # set occupancy using olx.xf.au.SetAtomOccupancy(id, value)
    olx.xf.au.SetAtomOccu(id, 1)
    # or U/Uiso using olx.xf.au.SetAtomU(id, *[U values])
    olx.xf.au.SetAtomU(id, 0.04)
  #olx.Fuse()
  olx.xf.EndUpdate()


OV.registerFunction(match_dbfrag)

def find_frag(name):
  for num, name in db.find_fragment_by_name(name):
    print(num, name)

OV.registerFunction(find_frag)
