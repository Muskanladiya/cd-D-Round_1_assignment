from server.env import SupportEnv

env = SupportEnv()

obs = env.reset()
print("Start:", obs)

done = False

while not done:
    msg = input("Agent: ")
    result = env.step({"message": msg})

    print("Env:", result["observation"])
    print("Reward:", result["reward"])

    done = result["done"]