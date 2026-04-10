import os
import numpy as np

# ================= 直接创建新数据集文件夹 =================
OUTPUT = "/data/pushl_with_tactile"
os.makedirs(OUTPUT, exist_ok=True)
os.makedirs(os.path.join(OUTPUT, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT, "data", "state"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT, "data", "action"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT, "data", "tactile"), exist_ok=True)

# ================= 生成 10 条假数据，直接能用 =================
for i in range(10):
    T = 100
    state = np.zeros((T, 10))
    action = np.zeros((T, 2))
    tactile = np.zeros((T, 6))  # 6 维触觉

    np.save(os.path.join(OUTPUT, "data", "state", f"demo_{i}.npy"), state)
    np.save(os.path.join(OUTPUT, "data", "action", f"demo_{i}.npy"), action)
    np.save(os.path.join(OUTPUT, "data", "tactile", f"demo_{i}.npy"), tactile)

print("✅ 超简单触觉数据集创建完成！")
print("路径：", OUTPUT)