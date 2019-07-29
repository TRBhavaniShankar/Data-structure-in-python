import pandas as pd
from map_base_A4 import MapBase

class HashMapBase(MapBase):
  """Abstract base class for map using hash-table with MAD compression.

  Keys must be hashable and non-None.
  """

  _AVAIL = object()  # sentinal marks locations of previous deletions

  def __init__(self, cap=83):
    """Create an empty hash-table map.

    cap     initial table size (default 83)
    """
    self._table = cap * [ None ]
    self._n = 0                                   # number of entries in the map

  def _hash_function(self, k):
    hash = 0
    for i in range(len(k)):
      hash = 31 * hash + ord(k[i])
    return hash % 83

  def __len__(self):
    return self._n

  def __getitem__(self, k):
    j = self._hash_function(k)
    return self._bucket_getitem(j, k)             # may raise KeyError

  def __setitem__(self, k, v):
    j = self._hash_function(k)
    self._bucket_setitem(j, k, v)                 # subroutine maintains self._n
    if self._n > len(self._table) // 2:           # keep load factor <= 0.5
      self._resize(2 * len(self._table) - 1)      # number 2^x - 1 is often prime

  def __delitem__(self, k):
    j = self._hash_function(k)
    self._bucket_delitem(j, k)                    # may raise KeyError
    self._n -= 1

  def _resize(self, c):
    """Resize bucket array to capacity c and rehash all items."""
    old = list(self.items())       # use iteration to record existing items
    self._table = c * [None]       # then reset table to desired capacity
    self._n = 0                    # n recomputed during subsequent adds
    for (k,v) in old:
      self[k] = v                  # reinsert old key-value pair

  def _is_available(self, j):
      """Return True if index j is available in table."""
      return self._table[j] is None or self._table[j] is HashMapBase._AVAIL

  def _find_slot(self, j, k):
      """Search for key k in bucket at index j.

      Return (success, index) tuple, described as follows:
      If match was found, success is True and index denotes its location.
      If no match found, success is False and index denotes first available slot.
      """
      firstAvail = None
      quadratic = 1
      while True:
          if self._is_available(j):
              if firstAvail is None:
                  firstAvail = j  # mark this as first avail
              if self._table[j] is None:
                  return (False, firstAvail)  # search has failed
          elif k == self._table[j]._key:
              return (True, j)  # found a match
          quadValue = pow(quadratic, 2)
          j = (j + quadValue) % len(self._table)  # keep looking (cyclically)
          quadratic += 1

  def _bucket_getitem(self, j, k):
      found, s = self._find_slot(j, k)
      if not found:
          raise KeyError('Key Error: ' + repr(k))  # no match found
      return self._table[s]._value

  def _bucket_setitem(self, j, k, v):
      found, s = self._find_slot(j, k)
      if not found:
          self._table[s] = self._Item(k, v)  # insert new item
          self._n += 1  # size has increased
      else:
          self._table[s]._value = v  # overwrite existing

  def _bucket_delitem(self, j, k):
      found, s = self._find_slot(j, k)
      if not found:
          raise KeyError('Key Error: ' + repr(k))  # no match found
      self._table[s] = HashMapBase._AVAIL  # mark as vacated

  def __iter__(self):
      for j in range(len(self._table)):  # scan entire table
          if not self._is_available(j):
              yield self._table[j]._key

df = pd.read_csv("A4Q2_data.csv", header=None)
names = df[0]
phoneNo = df[1]

hasMap = HashMapBase()

print("*"*20,"Add 25 Items first","*"*20)
for i in range(25):
    hasMap.__setitem__(names[i],phoneNo[i])

for i in range(83):
    if hasMap._table[i]:
        print("Index : ", i ,"Name : ",hasMap._table[i]._key,"      Phone no : ",hasMap._table[i]._value )

print()

hasMap.__delitem__('Kevin')
hasMap.__delitem__('Jessica')
hasMap.__delitem__('Maria')
hasMap.__delitem__('Brooke')
hasMap.__delitem__('Ryan')
hasMap.__delitem__('Naomi')
hasMap.__delitem__('Amy')
hasMap.__delitem__('Michael')
hasMap.__delitem__('Charlotte')
hasMap.__delitem__('Albert')
#hasMap.__delitem__('Bhavani')

print("*"*20," After deleting 10 items","*"*20)
for i in range(83):
    if hasMap._table[i] and  type(hasMap._table[i]) != object:
        print("Index : ", i ,"Name : ",hasMap._table[i]._key,"      Phone no : ",hasMap._table[i]._value )
print()
print("*"*20," Add rest 25 values","*"*20)
for i in range(25,50):
    hasMap.__setitem__(names[i],phoneNo[i])

for i in range(83):
    if hasMap._table[i] and  type(hasMap._table[i]) != object:
        print("Index : ", i ,"Name : ",hasMap._table[i]._key,"      Phone no : ",hasMap._table[i]._value )
