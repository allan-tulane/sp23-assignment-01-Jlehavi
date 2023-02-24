"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
        return foo(x-1) + foo(x-2)
    pass

def longest_run(mylist, key):
    high, count = 0
    for i in mylist:
      if i == key:
        count += 1
      elif count > high:
        high = count
      else:
        count = 0
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  finalObj = longest_run_recursive_helper(mylist, key)
  return finalObj.longest_size

def longest_run_recursive_helper(mylist, key):
  if len(mylist) == 0:
    return 0
  elif len(mylist) == 1 and mylist[0] == key:
    return Result(len(mylist)//2, len(mylist) - len(mylist)//2, 1,                      True)
  elif len(mylist) == 1:
    return Result(len(mylist)//2, len(mylist) - len(mylist)//2, 0,                      False)
  else:
    obj1 = longest_run_recursive(mylist[:len(mylist)//2], key)
    obj2 = longest_run_recursive(mylist[len(mylist)//2:], key)
    
    entireRange = obj1.is_entire_range and obj2.is_entire_range
  
    if entireRange:
      longestSize = obj1.longest_size + obj2.longest_size
    else:
      longestSize = max(obj1.longest_size, obj2.longest_size)
      
    finalObj = Result(obj1.left_size+obj1.right_size,               
                      obj2.left_size+obj2.right_size,
                      longestSize,
                      entireRange)
  
    return finalObj

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


