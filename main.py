import pandas as pd
import matplotlib.pyplot as plt
import json

# Read JSON data from the "items.json" file
with open('zoom_marketplace_2023-11-21.json', 'r') as file:
    data = json.load(file)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Create a list of all permissions required by apps
all_permissions = [scope for scopes in df['scopes'] for scope in scopes]

# Count the occurrences of each permission
permission_counts = pd.Series(all_permissions).value_counts()

# Plot the graph with adjusted figure size and spacing
plt.figure(figsize=(18, 8))  # Adjust the figure size as needed
permission_counts.plot(kind='bar', width=0.8, color='green')  # Adjust width and color as needed
plt.title('Number of Apps Requiring Each Type of Scope')
plt.xlabel('Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')  # Adjust rotation angle and alignment as needed
plt.tight_layout()  # Adjust layout for better spacing
plt.show()


# Print the results in the terminal
print("Permission Counts:")
print(permission_counts)
