import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import yaml

def setup_plot():

    sns.set_palette("husl")
    sns.set_style("white")
    sns.set_style("ticks")
    mpl.rcParams.update({'figure.autolayout': True})

  
    
    mpl.rcParams['font.family']= 'times'
    mpl.rcParams['font.weight']= 'normal'
    mpl.rcParams['font.size']= 16
    mpl.rcParams['font.size']= 16
    

    mpl.rcParams['xtick.labelsize'] = 16
    mpl.rcParams['ytick.labelsize'] = 16
    mpl.rcParams['legend.fontsize'] = 16
    mpl.rcParams['axes.titlesize'] = 16
    mpl.rcParams['axes.labelsize'] = 16

    # mpl.rcParams['figure.dpi'] = 30
    mpl.rcParams['savefig.dpi'] = 300
    mpl.rcParams['savefig.format'] = "png"
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.unicode']=True



setup_plot()

names = ["regen", "isotropic", "piola"]


fig = plt.figure()
ax = fig.gca()

for fname in names:
    
    with open("{}.yml".format(fname), "r") as f:
        d = yaml.load(f)


    res_u = d["res_u"]
    res_i = d["res_i"]

    ax.semilogy(res_u, label = "unloaded {}".format(fname))
    ax.semilogy(res_i, label = "loaded {}".format(fname))


ax.set_xlabel("$\#$ iterations")
ax.set_ylabel("Residual (cm)")
ax.legend(loc = "best")
fig.savefig("unloaded_error.png")
