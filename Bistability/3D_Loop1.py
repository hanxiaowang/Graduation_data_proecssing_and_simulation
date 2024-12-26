from Prepare import *


drive_power_in=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\CP in path 4\e\drive power.txt'));
delta_m_in=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\CP in path 4\e\drive fre.txt'));
# cpf_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 12-21-25\Delta omega up.txt'));
# cfp_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change frequency first 12-44-25\Delta omega up.txt'));
step_in=np.linspace(1,len(drive_power_in)+1,len(drive_power_in))
# print(len(step_in))
#
drive_power_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\drive power.txt'));
delta_m_up_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\drive fre.txt'));
# cpf_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\Delta omega up.txt'));
# cfp_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change frequency first 20-25-25\Delta omega up.txt'));
step_in_up=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))


plot_p_and_f(step_in,drive_power_in[::-1]*1e3,delta_m_in[::-1])