


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



columns_title = ["month_number", "facecream", "facewash", "toothpaste",
           "bathingsoap", "shampoo", "moisturizer", "total_units",
           "total_profit"]

data =[[1,2500,1500,5200,9200,1200,1500,21100,211000],
        [2,2630,1200,5100,6100,2100,1200,18330,183300],
        [3,2140,1340,4550,9550,3550,1340,22470,224700],
        [4,3400,1130,5870,8870,1870,1130,22270,222700],
        [5,3600,1740,4560,7760,1560,1740,20960,209600],
        [6,2760,1555,4890,7490,1890,1555,20140,201400],
        [7,2980,1120,4780,8980,1780,1120,29550,295500],
        [8,3700,1440,5860,9960,2860,1440,36140,361400],
        [9,3540,1780,6100,8100,2100,1780,23400,234000],
        [10,1990,1890,8300,10300,2300,1890,26670,266700],
        [11,2340,2100,7300,13300,2400,2100,41280,412800],
        [12,2900,1760,7400,14400,1800,1760,30020,300200]]

df = pd.DataFrame(data, columns = columns_title)

number = int(input("Please enter the plot that you want to see: "))


match number:
        case 1:

                fig, ax = plt.subplots(figsize = (9, 6))


                ax.scatter(x = df['month_number'], y = df['toothpaste'])
                ax.set(title = "Tooth paste Sales data" ,xlabel = "Month Number", ylabel = "Number of units Sold")
                ax.grid(linestyle = '--')
                ax.set_xticks(df['month_number'])

                plt.legend(["Tooth paste Sales data"])
                plt.show()



        case 2:
                fig, ax = plt.subplots(figsize = (8, 5))
                custom_yticks = [1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000]

                ax.plot(df['month_number'], df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']], marker = 'o', linewidth = 3)
                ax.set_xticks(df['month_number'])
                ax.set_yticks(custom_yticks)
                ax.set(title = "Sales Data" ,xlabel = "Month Number", ylabel = "Sales Units in number")


                plt.legend(['Face cream sales Data', 'Face Wash sales Data', 'ToothPaste Sales Data', 'Bathingsoap Sales Data', 'Shampoo Sales Data', 'Moisturizer Sales Data'])
                plt.show()


        case 3:
                fig, ax = plt.subplots(figsize = (8, 6))

                ax.bar(df['month_number'], df['bathingsoap'], 0.7)
                ax.grid(linestyle = '--')
                ax.set_xticks(df['month_number'])
                ax.set(title = 'bathingsoap sales data', xlabel = 'Month Number', ylabel = 'Sales units in number')


                plt.show()



        case 4:

                fig, ax = plt.subplots(figsize = (8, 5))




                ax.bar(df['month_number'] - 0.15, df['facecream'], 0.3, label = 'Face Cream sales data')
                ax.bar(df['month_number'] + 0.15, df['facewash'], 0.3, label = 'Face Wash sales data')
                ax.grid(linestyle = '--')
                ax.set_xticks(df['month_number'])
                ax.set(title = 'Facewash and facecream sales data', xlabel = 'Month Number', ylabel = 'Sales units in number')



                plt.legend(loc = 'upper left')
                plt.show()


        case 5:
                fig, ax = plt.subplots(figsize = (8, 8))

                labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']

                total_units = df['total_units'].tolist()
                face_cream = df['facecream'].tolist()
                facewash = df['facewash'].tolist()
                toothpaste = df['toothpaste'].tolist()
                bathingsoap = df['bathingsoap'].tolist()
                shampoo = df['shampoo'].tolist()
                moisturizer = df['moisturizer'].tolist()

                total_units = sum(total_units)
                lst = [sum(face_cream), sum(facewash), sum(toothpaste) ,sum(bathingsoap), sum(shampoo), sum(moisturizer)]

                values = [round(((value / total_units) * 100), 2) for value in lst]
                ax.pie(values, labels=labels, autopct = '%1.1f%%')

                ax.set(title = "Sales data")

                plt.legend(loc = 'lower right')
                plt.show()


        case 6:
                fig, ax = plt.subplots(figsize = (10, 6))

                custom_xticks = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
                custom_yticks = [0, 1, 2, 3, 4, 5]

                total_profit_lst = sorted(df['total_profit'].tolist())


                ax.hist(total_profit_lst, label = 'Profit data', bins = [175000, 200000, 225000, 250000, 300000, 350000])
                ax.set(title = 'Profit data', xlabel = 'profit range in dollar', ylabel = 'Actual Profit in dollar')
                ax.set_xticks(custom_xticks)
                ax.set_yticks(custom_yticks)
                

                plt.legend(loc = 'upper left')
                plt.show()

        case 7:
                fig, ax = plt.subplots(figsize = (10, 6))

                x_range = range(1, len(df['month_number']) + 1)

                ax.plot(x_range, df['total_profit'], 'o--', color = '#fe1b1b', linewidth = 4, label = "Profit data of last year", markersize = 10, markerfacecolor = 'black')
                ax.set(title = "Company Sales data of last year", xlabel = "Month Number")
                ax.set_yticks([100000, 200000, 300000, 400000, 500000])
                ax.set_xticks(x_range)

                plt.legend(loc = 'lower right', fontsize = 14)
                plt.plot()


        case 8:
                fig, (ax1, ax2) = plt.subplots(figsize = (10, 4), nrows = 2)

                ax1_range = range(1, len(df['bathingsoap']) + 1)

                ax1.plot(ax1_range, df['bathingsoap'], marker = 'o', color = 'black', linewidth = 4)
                ax1.set(title = "Sales data of a Bathingsoap", yticks = [12500, 10000, 7500],
                        xticks = ax1_range)
                ax1.tick_params('x', labelbottom = False)

                ax2_range = range(1, len(df['facewash']) + 1)

                ax2.plot(ax2_range, df['facewash'], marker = 'o', color = 'r', linewidth = 4)
                ax2.set(title = "Sales data of a facewash", yticks = [2000, 1500],
                        xticks = ax2_range, xlabel = 'Month Number',
                        ylabel = 'Sales units in number')

                plt.show()


        case 9:
                fig, ax = plt.subplots(figsize = (10, 6))

                ax_range = range(1, len(df['total_profit']) + 1)
                


                ax.plot(ax_range, df['total_profit'])
                ax.set(title = "Company profit per month", xlabel = "Month number")
                ax.set_xticks(ax_range)
                ax.set_yticks([100000, 200000, 300000, 400000, 500000])


                plt.show()


        case 10:
                
                def peer_to_peer_sum(lst1: list, lst2: list) -> None:
                        answer_lst = []
                        for index1, value1 in enumerate(lst1):
                                for index2, value2 in enumerate(lst2):
                                        if index1 == index2:
                                                answer_lst.append(value1 + value2)
                                
                        
                        return answer_lst


                fig, ax = plt.subplots(figsize = (10, 6))

                range_x = range(1, 13)
                range_x_fill = range(0, 12)
                LINE_WIDTH_VALUE = 7

                face_cream = df['facecream'].tolist()
                face_wash = peer_to_peer_sum(df['facewash'].tolist(), face_cream)
                toothpaste = peer_to_peer_sum(df['toothpaste'].tolist(), face_wash)
                bathingsoap = peer_to_peer_sum(df['bathingsoap'].tolist(), toothpaste)
                shampoo = peer_to_peer_sum(df['shampoo'].tolist(), bathingsoap)
                moisturizer = peer_to_peer_sum(df['moisturizer'].tolist(), shampoo)

                ax.plot(range_x ,face_cream, color = '#bf00bf', label = 'Face Cream', linewidth = LINE_WIDTH_VALUE)
                ax.plot(range_x ,face_wash, color = '#00bfbf', label = 'Face Wash', linewidth = LINE_WIDTH_VALUE)
                ax.plot(range_x ,toothpaste, color = '#ff0000', label = 'Tooth Paste', linewidth = LINE_WIDTH_VALUE)
                ax.plot(range_x ,bathingsoap, color = '#000000', label = 'bathingsoap', linewidth = LINE_WIDTH_VALUE)
                ax.plot(range_x ,shampoo, color = '#008000', label = 'shampoo', linewidth = LINE_WIDTH_VALUE)
                ax.plot(range_x ,moisturizer, color = '#bfbf00', label = 'moisturizer', linewidth = LINE_WIDTH_VALUE)

                ax.fill_between(range_x, face_cream, color = '#bf00bf')
                ax.fill_between(range_x, face_cream , face_wash, color = '#00bfbf')
                ax.fill_between(range_x, face_wash, toothpaste, color = '#ff0000')
                ax.fill_between(range_x, toothpaste, bathingsoap, color = '#000000')
                ax.fill_between(range_x, bathingsoap, shampoo, color = '#008000')
                ax.fill_between(range_x, shampoo, moisturizer, color = '#bfbf00')

                ax.set(title = "All product sales data using stack plot", xlabel = "Month Number",
                ylabel = "Sales units in Number", xticks = [2, 4, 6, 8, 10, 12],
                yticks = [0 ,5000, 10000, 15000, 20000, 25000, 30000])
                ax.set_ylim(0, 31000)
                ax.set_xlim(1, 12)

                plt.legend(fontsize = 15, loc = 'upper left')
                plt.show()



