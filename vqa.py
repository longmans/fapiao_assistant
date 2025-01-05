from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv(override=True)  # 从本地.env文件加载环境变量

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_image_description(image_path):
    base64_image = encode_image(image_path)
    client = OpenAI(
        api_key=os.getenv('DASHSCOPE_API_KEY'),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-vl-max-latest",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"}, 
                    },
                    {"type": "text", "text": "判断图片是否是发票（票据不是发票），如果是发票返回发票的价格（价税合计，如59.00），否则返回0。注意不要返回其他文本，只返回价格。"},
                ],
            }
        ],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    image_path = "./output_images/25449165851000000238_page_1.png"
    description = get_image_description(image_path)
    print(description)