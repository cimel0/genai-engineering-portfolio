import math
def cosine_similarity(u: list[float], v: list[float]) -> float: 
  dot_product= sum(a * b for a, b in zip(u, v))
  norm_u= math.sqrt(u[0]**2 + u[1]**2)
  norm_v= math.sqrt(v[0]**2 + v[1]**2)
  return dot_product/ (norm_u * norm_v)

hund=[0.9,0.8]
katze=[0.85,0.75]
auto=[0.1,0.9]

print(cosine_similarity(hund, katze))
print(cosine_similarity(hund, auto))