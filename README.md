# 发票统计助手

该项目用于递归读取`data`目录中的PDF文件，将其转换为图片，并使用大模型的API对图片进行分析，判断是否为发票并提取价格。

## 安装

1. 克隆项目到本地：
    ```bash
    git clone https://github.com/yourusername/fapiao_assistant.git
    cd fapiao_assistant
    ```

2. 创建并激活虚拟环境（可选）：
    ```bash
    python -m venv venv
    source venv/bin/activate  # 对于Windows用户，使用 `venv\Scripts\activate`
    ```

3. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```


## 配置

1. 在项目根目录下创建一个`.env`文件，并添加你的`DASHSCOPE_API_KEY`：
    ```env
    DASHSCOPE_API_KEY=your_api_key_here
    ```

    你可以通过[阿里云百炼API控制台](https://bailian.console.aliyun.com/)申请API Key。

## 使用

1. 确保`data`目录中有PDF文件。
2. 运行`main.py`脚本：
    ```bash
    python main.py
    ```

    该脚本将递归读取`data`目录中的PDF文件，将其转换为图片，并使用大模型的API对图片进行分析，判断是否为发票并提取价格。

## 目录结构

```
fapiao_assistant/
│
├── data/                   # 存放PDF文件的目录（创建一个目录，将你的发票pdf放到这个目录）
├── output_images/          # 存放转换后的图片（自动生成）
├── read_pdfs.py            # 读取PDF并转换为图片的脚本
├── vqa.py                  # 使用大模型 API对图片进行分析的脚本
├── main.py                 # 主脚本，整合所有功能
├── .env                    # 存放API Key的环境变量文件
└── requirements.txt        # 项目依赖
```

## 注意事项

- 确保`.env`文件中的`DASHSCOPE_API_KEY`正确无误。
- 确保`data`目录中有PDF文件。
