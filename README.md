# CS231n_learning

这是我学习 Stanford CS231n（Convolutional Neural Networks for Visual Recognition）时建立的个人作业归档仓库。

我把课程作业、Notebook 实验结果和学习笔记集中保存在这里，方便在学习过程中回顾实现细节、对照课程内容，并记录自己从传统图像分类模型到卷积神经网络的实践过程。仓库中的内容主要来自我的学习过程，不是课程官方仓库，也不是一份整理完成的教程或标准答案。

目前仓库整理了 Assignment 1 和 Assignment 2。后续如果继续完成课程内容，会沿用相同的目录结构补充新的作业与笔记。

## 已整理内容

- Assignment 1：k-nearest neighbor、线性分类器、Softmax、两层全连接网络等基础实现。
- Assignment 2：全连接网络、Batch Normalization、Dropout、卷积网络以及 PyTorch 实践等内容。
- Jupyter Notebook：记录实验过程、结果和必要的代码说明。
- Notes：整理学习过程中对模型、反向传播和实现细节的理解。

## 仓库结构

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

## 如何使用

建议按照课程作业顺序阅读对应 Notebook。每个 Assignment 都保留了相对独立的 `cs231n` Python 包，因此运行某个作业时，应将该作业目录作为工作目录；切换作业后建议重启 Jupyter 内核，避免导入到另一份同名包。

## 本地运行

推荐使用 VS Code 的 Python、Jupyter 扩展，或 JupyterLab。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name cs231n-learning --display-name "CS231n Learning"
```

选择上述内核后，在对应的 Assignment 目录中打开并运行 Notebook。PyTorch 的 CUDA 支持取决于本机显卡、驱动和安装的 PyTorch 版本。

Assignment1 和 Assignment2 都包含名为 `cs231n` 的 Python 包。运行时以对应作业文件夹为工作目录；切换作业时重启内核，避免加载到另一份同名包。

部分卷积操作需要编译 Cython 扩展。若当前环境需要使用该扩展，可在 Assignment2 的 `cs231n` 目录下执行：

```powershell
python setup.py build_ext --inplace
```

该步骤需要适用于当前 Python 环境的 C/C++ 编译工具。仓库保留 `.pyx` 源码，编译产物应在本机重新生成。

## 数据与实验记录

仓库保留部分 Notebook 中的实验输出，主要用于记录当时的学习过程。由于 Python、依赖库、数据和硬件环境可能不同，已有输出不保证在所有环境中完全复现；如需验证结果，请在本地重新运行 Notebook。

CIFAR-10、COCO 数据、预提取特征、模型权重、压缩包和缓存文件不纳入版本管理。数据下载脚本仍保留在各作业的 `cs231n/datasets` 目录中，具体数据路径以对应 Notebook 中的配置为准。
Windows 用户可通过 Git Bash 运行 `.sh` 脚本，或按照脚本中的地址手动下载并解压数据。

## 说明

- 本仓库仅用于个人学习和代码整理，作业模板中的题目、说明及来源信息尽量保持原样。
- 使用课程代码或数据时，请遵守 CS231n 课程及相关数据集的许可和学术规范。
- 如果你也在学习 CS231n，欢迎把这个仓库当作一个学习过程参考；其中的实现和笔记难免存在不足，建议结合课程讲义与官方作业说明理解。
