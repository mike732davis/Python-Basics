from matplotlib import pyplot as plt
plt.style.use('ggplot')
# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,dev_y,label='all developers',color='yellow')
plt.plot(ages_x,py_dev_y,label='python developer',color='blue')
plt.plot(ages_x,js_dev_y,label='java developer',color='red')
plt.xlabel('Ages')
plt.ylabel('median salary')
plt.title('median salary by age')
plt.legend()
plt.savefig('Plot Styles picture\ggplot')
plt.show()