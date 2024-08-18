import numpy as np
from LiBrH2O import Refrigerant  # 从 LiBrH2O 模块导入 Refrigerant 类

# 创建 Refrigerant 对象
water = Refrigerant('Water')
#r134a = Refrigerant('R134a')

# 指定压力值 (kPa)
pressures = [100, 150, 200, 250, 300]

# 计算并打印饱和温度
for refrigerant in [water]:
    print(f"\nResults for {refrigerant.name}:")
    for P in pressures:
        T_sat = refrigerant.saturation_temperature(P)
        if not np.isnan(T_sat):
            print(f"{refrigerant.name} at {P} kPa has a saturation temperature of {T_sat:.2f} K")
        else:
            print(f"Could not calculate saturation temperature for {refrigerant.name} at {P} kPa")
