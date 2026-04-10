import sys
sys.path.append("/data/state_diff-main")

from state_diff.env.block_pushing.block_pushing import BlockPushingEnv

env = BlockPushingEnv()
sim = env.sim

print("=== 所有 geom 名称 ===")
for i in range(sim.model.ngeom):
    name = sim.model.geom_id2name(i)
    if name is not None:
        print(f"{i}: {name}")