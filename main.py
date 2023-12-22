import pandas as pd
import matplotlib.pyplot as plt
import json

with open('zoom_marketplace_2023-11-21.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

scope_data = [scope for scopes in df['scopes'] for scope in scopes]
viewPermission_data = [wow for wows in df['viewPermissions'] for wow in wows]
managePermission_data = [wow for wows in df['managePermissions'] for wow in wows]

permission_counts = pd.Series(scope_data).value_counts()
test1 = pd.Series(viewPermission_data).value_counts()
test2 = pd.Series(managePermission_data).value_counts()

plt.figure(figsize=(18, 8))
permission_counts.plot(kind='bar', width=0.8, color='green')
plt.title('Number of Apps Requiring Each Type of Scope')
plt.xlabel('Scope Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

test1.plot(kind='bar', width=0.8, color='blue')
plt.title('Number of Apps Requiring Each Type of View Permission')
plt.xlabel('View Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

test2.plot(kind='bar', width=0.8, color='red')
plt.title('Number of Apps Requiring Each Type of Manage Permission')
plt.xlabel('Manage Permission')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


print("Scope Permission Counts:")
print(permission_counts)

print()
print("View Permission Counts:")
print(test1)

print()
print("Manage Permission Counts:")
print(test2)
