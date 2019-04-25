def comp(a, b):
      if a==None or b==None:
          return False
      else:
          squa=[]
          for i in a:
              squa.append(i**2)
          squasort=sorted(squa)
          bsort=sorted(b)
          if squasort==bsort:
              return True
          else:
              return False