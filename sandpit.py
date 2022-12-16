# import pandas as pd
#
# # create DataFrame
# df = pd.DataFrame({'team': ['A', 'A', 'A', 'B', 'B', 'C'],
#                    'conference': ['East', 'East', 'East', 'West', 'West', 'East'],
#                    'points': [11, 8, 10, 6, 6, 5]})
#
# for x in df.conference.unique():
#     print(x)
#
# # print((df.conference == 'East').sum())
# print(len((df.conference.unique())))
######################################################################################################################
# monthly_mean.plot(x=df.index, y='A')
# monthly_mean.plot(y='A')
# monthly_mean.reset_index().plot(x='index', y='A')
# monthly_mean.plot(y='A', use_index=True)
#####################################################################################################################
import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(10)
# y_bot = np.linspace(30, 50, 10)
# y_dif = np.linspace(10, 5, 10)
#
# plt.bar(x, y_dif, bottom=y_bot)
# plt.show()
######################################################################################################################
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
#
# t1 = np.arange(0.0, 5.0, 0.01)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# print(type(t1))
#
# plt.figure(1) # plt can store a lot of figures at once.
# # The subplot() command specifies numrows, numcols,
# # fignum where fignum ranges from 1 to numrows*numcols.
# plt.subplot(121) # no. of rows, no. of columns, plot 1
# plt.grid()
# plt.plot(t1, f(t1), 'b-')
#
# plt.subplot(122) # no. of rows, no. of columns, plot 2
# plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
#
# plt.figure(2)
# # The subplot() command specifies numrows, numcols,
# # fignum where fignum ranges from 1 to numrows*numcols.
# plt.subplot(211)
# plt.grid()
# plt.plot(t1, f(t1), 'b-')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
# plt.show()
#####################################################################################################################
