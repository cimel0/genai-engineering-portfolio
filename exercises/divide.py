def safe_divide(a:float, b: float) -> float | str:
  try: 
    result = a/b
    return result
  except ZeroDivisionError: 
    return "Division durch Null nicht erlaubt"

if __name__ == "__main__":
  print(safe_divide(100, 5)) 
