# 模块（Module）
[常用内置模块](./commonly_used_modules/commonly_used_built-in_modules.md)

[常用第三方模块](./commonly_used_modules/commonly_used_third_party_%20modules.md)
### 什么是模块？
模块是一组Python代码，包含函数、类、变量等定义，可以被其他程序导入使用。模块的作用主要有以下几点：

1. 代码重用：模块可以被其他程序导入使用，可以减少代码重复，提高代码的可维护性。
2. 命名空间管理：模块可以有效地管理命名空间，避免不同模块之间的命名冲突。
3. 包管理：模块可以被打包成包，方便管理和分发。

### 模块的导入
Python中，模块的导入使用`import`语句，语法如下：

```python
import module1[, module2[,... moduleN]]
```

导入模块后，可以使用模块名访问模块中的函数、类、变量等。
python所有内置函数、模块、类都被放在__builtins__模块中，可以直接使用。
参考：
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/modules.html
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/index.html

### 模块的搜索路径
Python解释器会搜索指定的路径来定位模块，搜索路径存储在`sys.path`变量中，可以通过`sys.path.append()`方法添加搜索路径。

### 模块的安装
Python提供了`pip`工具来安装第三方模块，语法如下：

```
pip install module_name
```

安装完成后，可以使用`import`语句导入模块。

### 模块的创建
模块的创建使用`__init__.py`文件，该文件必须存在于模块的目录中，文件内容可以为空。

模块的导入路径：

```
module_name/__init__.py
```

模块的导入路径可以是相对路径或绝对路径，但推荐使用绝对路径。
模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。