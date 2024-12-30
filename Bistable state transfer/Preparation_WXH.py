# rows[j] for rows in forward1

import os
import numpy as np
import datetime
import matplotlib.pyplot as plt
import json

class date_and_time():
    def __init__(self):
        self.curr_time = datetime.datetime.now()
        self.time_str = self.curr_time.strftime("%m%d")
        self.date = str(self.curr_time.year) + str(self.time_str)

    def ymd(self):
        return self.date

    def hms(self):
        time = str(self.curr_time.hour) + '-' + str(self.curr_time.minute) + '-' + str(self.curr_time.second)
        return time


class save_file(date_and_time):
    def __init__(self):
        super().__init__()
        # path = f'C:\\Users\\AORUS\\OneDrive\\桌面\\bistable date'
        # if os.path.exists(path) == True:
        #    pass
        # else:
        #     os.mkdir(path)

    def creat_initial_file(self, path: str):
        if os.path.exists(path) == True:
            pass
        else:
            os.mkdir(path)

    def creat_sub_file(self, path: str, name: str):
        sfile_name = os.path.join(path, name)
        if os.path.exists(sfile_name) == True:
            pass
        else:
            os.mkdir(sfile_name)
        return sfile_name

    def save_txt(self, path: str, name: str, list, fmt="%.10f"):
        txt_name = os.path.join(path, name + '.txt')
        np.savetxt(txt_name, list, fmt=fmt, delimiter=',')

    def save_anomalous_txt(self,path,name: str,list):
        txt_name = os.path.join(path, name + '.txt')
        with open(txt_name,'a') as f:
            for i in range(len(list)):
                for j in range(len(list[i])):
                    if j==(len(list[i])-1):
                        f.write(str(list[i][j])+'\n')
                    else:
                        f.write(str(list[i][j]) + ',')

    def read_anomalous_txt(self,path):
        output=[]
        x=open(path, "r")
        aa=x.readlines()
        for i in range(len(aa)):
            aaa = list(map(float, aa[i].split(',')))
            output.append(aaa)
        return output

    def save_npy(self, path: str, name: str, list: list):
        npy_name = os.path.join(path, name + '.npy')
        np.save(npy_name, arr=list)

    def save_json(self,path: str, name: str, dict):
        json_name = os.path.join(path, name + '.json')
        with open(json_name, "w") as fp:
            json.dump(dict, fp,indent=1)
        fp.close()

    def save_jpg(self, path: str, name: str):
        jpg_name = os.path.join(path, name + '.jpg')
        return jpg_name

    def save_svg(self, path: str, name: str):
        svg_name = os.path.join(path, name + '.svg')
        return svg_name

    def measurement_file(self, name: str):
        path = f'E:\\works\\experiment\\' + self.ymd() + f'\\' + name + ' ' + self.hms()
        self.creat_initial_file(path)
        print(path)
        return path


class Plot_easy():
    def __init__(self, **kwargs):
        self.x_name = kwargs.get('x_name', '')
        self.y_name = kwargs.get('y_name', '')
        self.z_name = kwargs.get('z_name', '')
        self.x1 = kwargs.get('x1', [])
        self.y1 = kwargs.get('y1', [])
        self.z1 = kwargs.get('z1', [])
        self.x2 = kwargs.get('x2', [])
        self.y2 = kwargs.get('y2', [])
        self.z2 = kwargs.get('z2', [])
        self.x3 = kwargs.get('x3', [])
        self.y3 = kwargs.get('y3', [])
        self.z3 = kwargs.get('z3', [])
        self.x4 = kwargs.get('x4', [])
        self.y4 = kwargs.get('y4', [])
        self.z4 = kwargs.get('z4', [])
        self.x5 = kwargs.get('x5', [])
        self.y5 = kwargs.get('y5', [])
        self.z5 = kwargs.get('z5', [])
        self.x6 = kwargs.get('x6', [])
        self.y6 = kwargs.get('y6', [])
        self.z6 = kwargs.get('z6', [])
        self.x7 = kwargs.get('x7', [])
        self.y7 = kwargs.get('y7', [])
        self.z7 = kwargs.get('z7', [])
        self.x8 = kwargs.get('x8', [])
        self.y8 = kwargs.get('y8', [])
        self.z8 = kwargs.get('z8', [])


        self.path = kwargs.get('path', '')

        self.linestyle1 = kwargs.get('linestyle1', 'point')
        self.linestyle2 = kwargs.get('linestyle2', 'point')
        self.linestyle3 = kwargs.get('linestyle3', 'point')
        self.linestyle4 = kwargs.get('linestyle4', 'point')
        self.linestyle5 = kwargs.get('linestyle5', 'point')
        self.linestyle6 = kwargs.get('linestyle6', 'point')
        self.linestyle7 = kwargs.get('linestyle7', 'point')
        self.linestyle8 = kwargs.get('linestyle8', 'point')
        self.point1 = kwargs.get('point1', 'o-')
        self.point2 = kwargs.get('point2', 'o-')
        self.point3 = kwargs.get('point3', 'o-')
        self.point4 = kwargs.get('point4', 'o-')
        self.point5 = kwargs.get('point5', 'o-')
        self.point6 = kwargs.get('point6', 'o-')
        self.point7 = kwargs.get('point7', 'o-')
        self.point8 = kwargs.get('point8', 'o-')

        self.label1 = kwargs.get('label1', '')
        self.label2 = kwargs.get('label2', '')
        self.label3 = kwargs.get('label3', '')
        self.label4 = kwargs.get('label4', '')
        self.label5 = kwargs.get('label5', '')
        self.label6 = kwargs.get('label6', '')
        self.label7 = kwargs.get('label7', '')
        self.label8 = kwargs.get('label8', '')
        self.title = kwargs.get('title', '')
        self.color1 = kwargs.get('color1', 'black')
        self.color2 = kwargs.get('color2', 'blue')
        self.color3 = kwargs.get('color3', 'yellowgreen')
        self.color4 = kwargs.get('color4', 'red')
        self.color5 = kwargs.get('color5', 'olive')
        self.color6 = kwargs.get('color6', 'purple')
        self.color7 = kwargs.get('color7', 'deeppink')
        self.color8 = kwargs.get('color8', 'darkcyan')
        self.size1 = kwargs.get('size1', '5')
        self.size2 = kwargs.get('size2', '5')
        self.size3 = kwargs.get('size3', '5')
        self.size4 = kwargs.get('size4', '5')
        self.size5 = kwargs.get('size5', '5')
        self.size6 = kwargs.get('size6', '5')
        self.size7 = kwargs.get('size7', '5')
        self.size8 = kwargs.get('size8', '5')

        self.switch = kwargs.get('switch','off')

    def Plot_1D(self, **kwargs):
        plt.figure()
        if self.x1 is not None:
            if self.linestyle1 == 'point':
                plt.plot(self.x1, self.y1, self.point1, markerfacecolor='none', color=self.color1,markersize=self.size1, label=self.label1)
            else:
                plt.plot(self.x1, self.y1, '-', color=self.color1,linewidth=self.size1 ,label=self.label1)

        if self.x2 is not None:
            if self.linestyle2 == 'point':
                plt.plot(self.x2, self.y2, self.point2, markerfacecolor='none', color=self.color2,markersize=self.size2, label=self.label2)
            else:
                plt.plot(self.x2, self.y2, '-', color=self.color2,linewidth=self.size2 ,label=self.label2)
        if self.x3 is not None:
            if self.linestyle3 == 'point':
                plt.plot(self.x3, self.y3, self.point3, markerfacecolor='none', color=self.color3,markersize=self.size3, label=self.label3)
            else:
                plt.plot(self.x3, self.y3, '-', color=self.color3,linewidth=self.size3 ,label=self.label3)
        if self.x4 is not None:
            if self.linestyle4 == 'point':
                plt.plot(self.x4, self.y4, self.point4, markerfacecolor='none', color=self.color4,markersize=self.size4, label=self.label4)
            else:
                plt.plot(self.x4, self.y4, '-', color=self.color4,linewidth=self.size4 ,label=self.label4)
        if self.x5 is not None:
            if self.linestyle5 == 'point':
                plt.plot(self.x5, self.y5, self.point5, markerfacecolor='none', color=self.color5,markersize=self.size5, label=self.label5)
            else:
                plt.plot(self.x5, self.y5, '-', color=self.color5,linewidth=self.size5 ,label=self.label5)
        if self.x6 is not None:
            if self.linestyle6 == 'point':
                plt.plot(self.x6, self.y6, self.point6, markerfacecolor='none', color=self.color6,markersize=self.size6, label=self.label6)
            else:
                plt.plot(self.x6, self.y6, '-', color=self.color6,linewidth=self.size6 ,label=self.label6)
        if self.x7 is not None:
            if self.linestyle7 == 'point':
                plt.plot(self.x7, self.y7, self.point7, markerfacecolor='none', color=self.color7,markersize=self.size7, label=self.label7)
            else:
                plt.plot(self.x7, self.y7, '-', color=self.color7,linewidth=self.size7 ,label=self.label7)
        if self.x8 is not None:
            if self.linestyle8 == 'point':
                plt.plot(self.x8, self.y8, self.point8, markerfacecolor='none', color=self.color8,markersize=self.size8, label=self.label8)
            else:
                plt.plot(self.x8, self.y8, '-', color=self.color8,linewidth=self.size8 ,label=self.label8)
        plt.xlabel(self.x_name, size=10)
        plt.ylabel(self.y_name, size=10)
        plt.legend()
        if len(self.title) != 0:
            plt.title(self.title)
        else:
            plt.title(self.y_name + ' vs ' + self.x_name)

        plt.rcParams['savefig.dpi'] = 600
        if len(self.path) != 0:
            plt.savefig(self.path)
        plt.show()
        if self.switch=='off':
            plt.close()
        else:
            pass

    def Plot_2D(self, **kwargs):
        cmap = kwargs.get('cmap', 'viridis')

        # extent = (min(self.x1), max(self.x1), min(self.y1), max(self.y1))
        plt.figure(figsize=(4, 4))
        ax1 = plt.subplot(111)
        gci1 = ax1.pcolor(self.x1,self.y1,self.z1,cmap=cmap)
        # gci1 = ax1.imshow(self.z1, extent=extent, origin='lower', aspect='auto', cmap=cmap)
        cbar = plt.colorbar(gci1)
        cbar.set_label(self.z_name, size=10)
        ax1.set_xlabel(self.x_name, size=10)
        ax1.set_ylabel(self.y_name, size=10)
        if self.title is not None:
            ax1.set_title(self.title)
        else:
            ax1.set_title(self.z_name + ' vs ' + self.x_name + ' and ' + self.y_name, fontsize=14)

        plt.tick_params(labelsize=10)
        cbar.ax.tick_params(labelsize=10)

        plt.rcParams['savefig.dpi'] = 600
        if len(self.path) != 0:
            plt.savefig(self.path)
        plt.show()
        if self.switch=='off':
            plt.close()
        else:
            pass

    def Plot_line_3D(self, **kwargs):

        fig=plt.figure()
        ax = fig.gca(projection='3d')
        if self.x1 is not None:
            if self.linestyle1 == 'point':
                ax.plot(self.x1, self.y1, self.z1, self.point1, markerfacecolor='none', color=self.color1, markersize=self.size1,label=self.label1)
            else:
                ax.plot(self.x1, self.y1, self.z1, '-', color=self.color1, linewidth=self.size1,label=self.label1)

        if self.x2 is not None:
            if self.linestyle2 == 'point':
                ax.plot(self.x2, self.y2, self.z2, self.point2, markerfacecolor='none', color=self.color2, label=self.label2)
            else:
                ax.plot(self.x2, self.y2, self.z2, '-', color=self.color2, linewidth=self.size2,label=self.label2)
        if self.x3 is not None:
            if self.linestyle3 == 'point':
                ax.plot(self.x3, self.y3, self.z3, self.point3, markerfacecolor='none', color=self.color3, label=self.label3)
            else:
                ax.plot(self.x3, self.y3, self.z3, '-', color=self.color3,linewidth=self.size3, label=self.label3)
        if self.x4 is not None:
            if self.linestyle1 == 'point':
                ax.plot(self.x4, self.y4, self.z4, self.point4, markerfacecolor='none', color=self.color4, label=self.label4)
            else:
                ax.plot(self.x4, self.y4, self.z4, '-', color=self.color4, linewidth=self.size4,label=self.label4)
        if self.x5 is not None:
            if self.linestyle5 == 'point':
                ax.plot(self.x5, self.y5, self.z5, self.point5, markerfacecolor='none', color=self.color5, label=self.label5)
            else:
                ax.plot(self.x5, self.y5, self.z5, '-', color=self.color5, linewidth=self.size5,label=self.label5)
        if self.x6 is not None:
            if self.linestyle6 == 'point':
                ax.plot(self.x6, self.y6, self.z6, self.point6, markerfacecolor='none', color=self.color6, label=self.label6)
            else:
                ax.plot(self.x6, self.y6, self.z6, '-', color=self.color6, linewidth=self.size6,label=self.label6)
        if self.x7 is not None:
            if self.linestyle7 == 'point':
                ax.plot(self.x7, self.y7, self.z7, self.point7, markerfacecolor='none', color=self.color7, label=self.label7)
            else:
                ax.plot(self.x7, self.y7, self.z7, '-', color=self.color7, linewidth=self.size7,label=self.label7)
        if self.x8 is not None:
            if self.linestyle8 == 'point':
                ax.plot(self.x8, self.y8, self.z8, self.point8, markerfacecolor='none', color=self.color8, label=self.label8)
            else:
                ax.plot(self.x8, self.y8, self.z8, '-', color=self.color8, linewidth=self.size8,label=self.label8)
        ax.set_xlabel(self.x_name, size=10)
        ax.set_ylabel(self.y_name, size=10)
        ax.set_zlabel(self.z_name, size=10)
        ax.legend()
        if len(self.title) != 0:
            ax.set_title(self.title)
        else:
            ax.set_title(self.x_name + ' + ' + self.y_name + ' vs ' + self.z_name)
        if len(self.path) != 0:
            ax.figure.savefig(self.path,dpi=600)
        # ax.show()
        if self.switch=='off':
            plt.close()
        else:
            pass


class Read_file():
    def __init__(self):
        pass

    def read_json(self,path):
        f = open(path, 'r')
        # print(f.read())
        data=f.read()
        return data

    def read_txt(self,path):
        data = np.loadtxt(path)
        return data

    def read_combation(self,init_path,sub_path):
        path = os.path.join(init_path, sub_path)
        data = np.loadtxt(path,delimiter=',')
        return data

    def read_npy(self,path):
        data=np.load(path)
        return data


class Combination():
    def __init__(self):
        pass

    def Array_two_1D(self,a,b):
        t=np.concatenate((a,b))
        return t

    def Array_three_1D(self,a,b,c):
        t=np.concatenate((a,b,c))
        return t

