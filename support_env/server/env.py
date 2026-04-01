class SupportEnv:
    def __init__(self):
        self.done = False

    def reset(self):
        self.done = False
        return {"message": "User: My order is delayed."}

    def step(self, action):
        user_input = action.get("message", "").lower()

        if "sorry" in user_input:
            self.done = True
            return {
                "observation": {"message": "User: Thanks for helping!"},
                "reward": 1,
                "done": True,
            }
        else:
            return {
                "observation": {"message": "User: Please resolve quickly!"},
                "reward": 0,
                "done": False,
            }