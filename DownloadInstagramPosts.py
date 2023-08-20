#

#pip install instaloader

import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Define the target Instagram profile
target_profile = "instagram"

# Download posts from the profile
loader.download_profile(target_profile, profile_pic=False, fast_update=True)

print("Posts downloaded successfully!")
