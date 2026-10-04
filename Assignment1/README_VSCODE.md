# 在 VS Code 中运行 kNN 作业

1. 在 VS Code 中打开整个 `assignment1` 文件夹。
2. 安装 Python、Jupyter 两个 VS Code 扩展。
3. 在终端创建并启用虚拟环境：

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python -m ipykernel install --user --name cs231n-assignment1 --display-name "CS231n Assignment 1"
   ```

4. 打开 `knn.ipynb`，点击右上角的内核选择器，选择 `CS231n Assignment 1`。
5. 从上到下运行单元格。首个代码单元会自动定位项目目录；如果 CIFAR-10 尚未存在，它会下载并解压数据集。

数据集最终应位于：

```text
cs231n/datasets/cifar-10-batches-py/
```

课程作业中的 `TODO` 保持原样，需要按题目要求自行完成。
