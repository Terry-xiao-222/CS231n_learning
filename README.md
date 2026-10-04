# CS231n_learning

CS231n 学习记录，收录 Assignment1、Assignment2 的代码、Jupyter Notebook 和个人笔记。目录名称沿用本地作业结构。

## 目录

```text
CS231n_learning/
├── Assignment1/
│   ├── cs231n/                 # 分类器、网络层、优化器等实现
│   ├── Notes/                  # 个人学习笔记
│   ├── knn.ipynb
│   ├── softmax.ipynb
│   ├── two_layer_net.ipynb
│   ├── features.ipynb
│   └── FullyConnectedNets.ipynb
├── Assignment2/
│   ├── cs231n/                 # 网络层、CNN、RNN 等实现
│   ├── BatchNormalization.ipynb
│   ├── Dropout.ipynb
│   ├── ConvolutionalNetworks.ipynb
│   ├── PyTorch.ipynb
│   └── RNN_Captioning_pytorch.ipynb
├── requirements.txt
└── .gitignore
```

## 本地运行

推荐使用 VS Code 的 Python、Jupyter 扩展，或 JupyterLab。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name cs231n-learning --display-name "CS231n Learning"
```

选择上述内核，从上到下运行对应 Notebook。PyTorch 的 CUDA 支持取决于本机显卡、驱动和安装的 PyTorch 版本。

Assignment1 和 Assignment2 都包含名为 `cs231n` 的 Python 包。运行时以对应作业文件夹为工作目录；切换作业时重启内核，避免加载到另一份同名包。

部分卷积操作需要编译 Cython 扩展。在 Assignment2 的 `cs231n` 目录下执行：

```powershell
python setup.py build_ext --inplace
```

该步骤需要适用于当前 Python 环境的 C/C++ 编译工具。仓库保留 `.pyx` 源码，编译产物应在本机重新生成。

## 数据与实验记录

仓库保留 Notebook 中已有的实验输出，以及 `cs231n/notebook_images` 中的教学图片。已有输出是历史记录，不代表在所有环境中均可复现；实际结果以重新运行 Notebook 为准。

CIFAR-10、COCO 数据、预提取特征、模型权重、压缩包和缓存不纳入版本管理。下载脚本保留在各作业的 `cs231n/datasets` 目录中，具体数据路径以对应 Notebook 为准。Windows 用户可通过 Git Bash 运行 `.sh` 脚本，或按脚本中的地址手动下载并解压。

本仓库用于个人学习，作业模板中的题目、说明和来源信息保持原样。
