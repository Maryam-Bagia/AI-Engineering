import matplotlib.pyplot as plt

# Data: Episodes or mission deployment points of ERPB in 'Teach You a Lesson'
episodes = [
    'Ep 1: Politician\'s Son',
    'Ep 2: School Gangs',
    'Ep 3: Influencer Fraud',
    'Ep 4: Elite Med-School',
    'Ep 5: Systemic Reform'
]

# Number of disciplinary actions / interventions handled by ERPB inspectors
interventions_count = [12, 19, 8, 15, 24]

# Create figure and axis
plt.figure(figsize=(9, 5))

# Plot bar chart
bars = plt.bar(episodes, interventions_count, color='#1f77b4', edgecolor='black', alpha=0.85)

# Customize chart details
plt.title('ERPB Interventions Across Episodes - "Teach You a Lesson"', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Series Episodes / Focus Areas', fontsize=11, labelpad=10)
plt.ylabel('Number of Disciplinary Actions', fontsize=11, labelpad=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add data values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, int(yval), ha='center', va='bottom', fontweight='bold')

# Set Y-axis limit to give breathing room for text labels
plt.ylim(0, 30)

# Display the plot
plt.tight_layout()
plt.show()