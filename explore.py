from lerobot.datasets.lerobot_dataset import LeRobotDataset

ds = LeRobotDataset("lerobot/pusht")
print("episodes:", ds.num_episodes)
print("frames:", ds.num_frames)
print("fps:", ds.fps)

sample = ds[0]
for k, v in sample.items():
    print(k, getattr(v, "shape", v))
