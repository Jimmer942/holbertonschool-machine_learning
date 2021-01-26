#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.xlim(0, 100, 10)
plt.xticks(np.arange(0, 110, 10))
plt.ylim(0, 30)
plt.title('Project A')
plt.hist(student_grades, edgecolor='black')
plt.show()
