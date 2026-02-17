import matplotlib.pyplot as plt
# Data 
months = list(range(1, 13)) # 1 to 12 
sales = [1000, 1200, 1500, 1800, 2100, 2400, 2300, 2500, 2700, 2900, 3100, 3300] 
# Create the plot 
plt.figure(figsize=(10, 6)) 
plt.plot(months, sales, marker='o', linestyle='-', color='b', linewidth=2,
markersize=8) 
# Customize the plot 
plt.title('Monthly Sales Data', fontsize=16) 
plt.xlabel('Month', fontsize=12) 
plt.ylabel('Sales ($)', fontsize=12) 
plt.grid(True, linestyle='--', alpha=0.7) 
# Customize x-axis ticks 
plt.xticks(months) 
# Add text annotations for start and end points 
plt.text(1, 1000, f'${sales[0]}', ha='right', va='bottom') 
plt.text(12, 3300, f'${sales[-1]}', ha='left', va='top')
# Show the plot plt.tight_layout() 
plt.show()
"""
unsure how this works go back after tutorial completed
"""