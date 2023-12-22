import pandas as pd
import matplotlib.pyplot as plt
import json

with open('zoom_marketplace_2023-11-21.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

scope_data = [scope for scopes in df['scopes'] for scope in scopes]
viewPermission_data = [vp for vps in df['viewPermissions'] for vp in vps]
managePermission_data = [mp for mps in df['managePermissions'] for mp in mps]

scope_permission = pd.Series(scope_data).value_counts()
view_permission = pd.Series(viewPermission_data).value_counts()
manage_permission = pd.Series(managePermission_data).value_counts()

plt.figure(figsize=(18, 8))
scope_permission.plot(kind='bar', width=0.8, color='green')
plt.title('Number of Apps Requiring Each Type of Scope')
plt.xlabel('Scope Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

view_permission.plot(kind='bar', width=0.8, color='blue')
plt.title('Number of Apps Requiring Each Type of View Permission')
plt.xlabel('View Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

manage_permission.plot(kind='bar', width=0.8, color='red')
plt.title('Number of Apps Requiring Each Type of Manage Permission')
plt.xlabel('Manage Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("Scope Permission Counts:")
print(scope_permission)

print()
print("View Permission Counts:")
print(view_permission)

print()
print("Manage Permission Counts:")
print(manage_permission)
