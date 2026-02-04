
class EllipticCurve:
  def __init__(self, p, a, b, n=None):
    self.p = int(p, 16)
    self.a = int(a, 16) % self.p
    self.b = int(b, 16) % self.p
    self.n = int(n, 16) % self.p
    if (4 * self.a**3 + 27 * self.b**2) % self.p == 0:
      print("Помилка: крива є сингулярною.")

  def IsOnCurve(curve, X, Y, Z=None):
    if Z == None:
      Z = 1
    q = curve.p
    return Y**2 * Z % q == (X**3 % q + curve.a * X * Z**2 % q + curve.b * Z**3 % q) % q
