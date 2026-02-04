
import random

class CurvePoint:
  def __init__(self, curve, X, Y, Z=None):
    self.curve = curve
    self.X = int(X, 16) % curve.p if isinstance(X, str) else X % curve.p
    self.Y = int(Y, 16) % curve.p if isinstance(Y, str) else Y % curve.p
    if Z != None:
      self.Z = int(Z, 16) % curve.p if isinstance(Z, str) else Z % curve.p
    else: self.Z = None
    if self.curve.IsOnCurve(self.X, self.Y, self.Z) == False:
      print("Помилка: точка не належить заданій еліптичній кривій.")

  def POINT_AT_INFINITY(Point):
    return CurvePoint(Point.curve, 0, 1, 0)

  def ComparePoints(Point1, Point2):
    z_inv1 = 1
    z_inv2 = 1
    if Point1.Z != None:
        z_inv1 = pow(Point1.Z, -1, Point1.curve.p)
    if Point2.Z != None:
        z_inv2 = pow(Point2.Z, -1, Point2.curve.p)
    if Point1.X * z_inv1 % Point1.curve.p != Point2.X * z_inv2 % Point2.curve.p:
      return False
    if Point1.Y * z_inv1 % Point1.curve.p != Point2.Y * z_inv2 % Point2.curve.p:
      return False
    return True

  def Print(Point):
    if Point.Z == None:
      print(f"({hex(Point.X)}, {hex(Point.Y)})")
    else:
      print(f"({hex(Point.X)}, {hex(Point.Y)}, {hex(Point.Z)})")

  def ToAffine(Point):
    if Point.Z == 0:
      return None
    z_inv = pow(Point.Z, -1, Point.curve.p)
    x = Point.X * z_inv % Point.curve.p
    y = Point.Y * z_inv % Point.curve.p
    return CurvePoint(Point.curve, x, y)

  def ToProjective(Point):
    return CurvePoint(Point.curve, Point.X, Point.Y, 1)

  def GenPoint(G):
    rand = random.randint(1, G.curve.n)
    return G.PointMultiply(rand)

  def PointDouble(Point):
    X, Y, Z, q = Point.X, Point.Y, Point.Z, Point.curve.p
    if Z == 0:
      return Point.POINT_AT_INFINITY()
    if Y == 0:
      return Point.POINT_AT_INFINITY()
    if Z == None:
      Z = 1

    W = (Point.curve.a * Z**2 + 3 * X**2) % q
    S = Y * Z % q
    B = X * Y * S % q
    H = (W**2 - 8 * B) % q
    X_ = 2 * H * S % q
    Y_ = (W * (4 * B - H) - 8 * Y**2 * S**2) % q
    Z_ = 8 * S**3 % q
    new_Point = CurvePoint(Point.curve, X_, Y_, Z_)
    return new_Point

  def PointAdd(Point1, Point2):
    X1, Y1, Z1 = Point1.X, Point1.Y, Point1.Z
    X2, Y2, Z2 = Point2.X, Point2.Y, Point2.Z
    q = Point1.curve.p
    if Z1 == 0:
      return Point2
    elif Z2 == 0:
      return Point1
    if Z1 == None:
      Z1 = 1
    if Z2 == None:
      Z2 = 1

    U1 = Y2 * Z1 % q
    U2 = Y1 * Z2 % q
    V1 = X2 * Z1 % q
    V2 = X1 * Z2 % q
    if V1 == V2:
      if U1 != U2:
        return Point1.POINT_AT_INFINITY()
      else:
        return Point1.PointDouble()
    U = (U1 - U2) % q
    V = (V1 - V2) % q
    W = Z1 * Z2 % q
    A = (U**2 * W - V**3 - 2 * V**2 * V2) % q
    X3 = V * A % q
    Y3 = (U * (V**2 * V2 - A) - V**3 * U2) % q
    Z3 = V**3 * W % q
    new_Point = CurvePoint(Point1.curve, X3, Y3, Z3)
    return new_Point

  def PointMultiply(Point, k):
    R0 = Point.POINT_AT_INFINITY()
    R1 = Point
    if R1.Z == None:
      R1 = R1.ToProjective()
    bits = bin(k)[2:]
    for i in range(0, len(bits)):
      if bits[i] == '0':
        R1 = R0.PointAdd(R1)
        R0 = R0.PointDouble()
      else:
        R0 = R0.PointAdd(R1)
        R1 = R1.PointDouble()
    return R0
