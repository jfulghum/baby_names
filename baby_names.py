import glob
import pandas as pd

 # echo 'State,Gender,Year,Name,Frequency' >00.TXT
 # cat 00.TXT
 # cat *.TXT >combined.csv # creating one big file
 # wc -l combined.csv # wc word count, can also count lines

df = pd.read_csv("combined.csv")

print(df.head)

# df2 = pd.read_csv('/Users/johannafulghum/Documents/Metis/namesbystate/' + states[0] +'.TXT')
# for state in states[1:]:
#     df = pd.read_csv('/Users/johannafulghum/Documents/Metis/namesbystate/' + state +'.TXT')
#     df2 = pd.concat([df2, df])
#
#
# print(df2)
#datafiles = '/Users/johannafulghum/Documents/Metis/namesbystate'


# frame = pd.DataFrame()
# total_list = []
# for textfile_ in datafiles:
#     df = pd.read_csv(textfile_, index_col=None, header=0)
#     total_list.append(df)
#
# frame = pd.concat(total_list)
# print(frame)
#

#
#
# names_all = []
#
# for year in range(1880,2014+1):
#     names_all.append(pd.read_csv('names/yob{}.txt'.format(year),names=['name','sex','number']))
#     names_all[-1]['year'] = year
#
# allyears = pd.concat(names_all)
#
#
# def sumsq(x):
#     return sum(x**2)
#
# spikyness = allyears.groupby(['sex','name'])['number'].agg(sumsq) / totals**2
