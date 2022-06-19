"""
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMIは10以上40以下 <- 常識的な範囲
        - 表示するときは小数点第2位まで
            - ex: 23.689 => 23.69
            - ex: 23.681 => 23.68
    できること:
        - BMIの計算
"""


class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.value = self.weight / (self.height**2)
        if not (10 <= self.value <= 40):
            raise ValueError(f"{self.value} BMIは範囲外です")

    def __str__(self):
        return f"{self.value:.2f}"            


tanaka_bmi = BMI(height=1.80, weight=30.0)
sasami_bmi = BMI(height=1.58, weight=40.0)


#  tanaka_bmiの出力
print(tanaka_bmi.height)
print(tanaka_bmi.value)
print(tanaka_bmi)

  #  def calculate_bmi(self):
        #  BMI ＝ 体重kg ÷ (身長m)2
      #  return self.weight / (self.height**2)
