import numpy as np
# 导入你刚刚修改的归一化环境
from state_diff.env.block_pushing.block_pushing import BlockPushNormalized

def run_test():
    print("⏳ 正在初始化 PyBullet 仿真环境...")
    # 实例化环境
    env = BlockPushNormalized()

    # 重置环境，获取初始状态
    state = env.reset()
    print("✅ 环境初始化成功！")
    print(f"👉 初始触觉力读数: {state.get('tactile_force')} (预期应为 [0. 0.])")

    print("\n🤖 开始执行随机动作测试，等待机械臂碰到方块...")
    contact_count = 0

    # 让机械臂随机动 200 步，总大概率能撞到一次方块
    for i in range(200):
        # 从动作空间随机采样一个合法动作
        action = env.action_space.sample()
        # 执行动作，获取下一步状态
        state, reward, done, info = env.step(action)

        # 提取当前的触觉力
        tactile = state.get('tactile_force')
        
        # 如果法向力（第0个元素）大于0，说明发生了接触
        if tactile is not None and tactile[0] > 0:
            print(f"💥 [第 {i} 步] 发生接触！法向力: {tactile[0]:.4f}, 摩擦力: {tactile[1]:.4f}")
            contact_count += 1
            
            # 成功打印 5 次接触记录后就停止测试
            if contact_count >= 5: 
                print("\n🎉 恭喜！测试完美通过！触觉信号提取与透传完全成功！")
                break

    if contact_count == 0:
        print("\n😅 跑了200步机械臂刚好没随机碰到方块，或者没遇到足够大的阻力。可以再运行一次试试！")

if __name__ == "__main__":
    run_test()
