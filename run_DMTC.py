import os

os.system("python B-net.py --config cfgs/Cifar-100/inter.yaml && "
          "python W-net.py --config cfgs/Cifar-100/t1.yaml && "
          "python W-net.py --config cfgs/Cifar-100/t2.yaml && "
          "python W-net.py --config cfgs/Cifar-100/t3.yaml")