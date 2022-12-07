class User:
    def __init__(self, initial_pts=1, final_pts=1, lead_time=1, method="на аккаунте", min_days=1, max_days=2,
                 first_sum=1, final_sum=1):
        self.initial_pts = initial_pts
        self.final_pts = final_pts
        self.lead_time = lead_time
        self.method = method
        self.min_days = min_days
        self.max_days = max_days
        self.first_sum = first_sum
        self.final_sum = final_sum