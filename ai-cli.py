#!/usr/bin/env python3
"""AI CLI 文档助手 —— 终端里一行命令，AI 自动整理文档"""
import os, sys, json
import urllib.request

KEY = os.environ.get("DEEPSEEK_KEY")
if not KEY:
    print("错误：请设置环境变量 DEEPSEEK_KEY")
    print("  setx DEEPSEEK_KEY sk-你的密钥")
    sys.exit(1)
API = "https://api.deepseek.com/v1/chat/completions"

MODES = {
    "summary": "你是文档摘要助手。输入文档，输出：一句话概括 + 核心要点 + 关键数据。简洁中文。",
    "requirements": "你是项目需求整理助手。输入客户原话，输出：核心需求 + 功能点拆解 + 待确认疑问 + 下一步建议。不猜测，不确定性放进疑问。中文。",
    "minutes": "你是会议纪要助手。输入会议内容，输出：概要 + 讨论要点 + 决策事项 + 待办清单。中文。"
}

def chat(system_prompt, user_text):
    data = json.dumps({
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        "temperature": 0.3, "max_tokens": 4096
    }, ensure_ascii=False).encode('utf-8')

    req = urllib.request.Request(API, data=data, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KEY}"
    })

    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read())
        return body["choices"][0]["message"]["content"]

def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python ai-cli.py summary     # 文档摘要")
        print("  python ai-cli.py requirements # 需求整理")
        print("  python ai-cli.py minutes     # 会议纪要")
        print("  echo 你的内容 | python ai-cli.py summary  # 管道输入")
        sys.exit(1)

    mode = sys.argv[1]
    if mode not in MODES:
        print(f"未知模式: {mode}，可选: {', '.join(MODES.keys())}")
        sys.exit(1)

    # Read input: file argument, then piped content, then prompt
    def read_file(path):
        for enc in ['utf-8', 'gbk', 'gb2312', 'utf-8-sig']:
            try:
                with open(path, 'r', encoding=enc) as f:
                    return f.read().strip()
            except UnicodeDecodeError:
                continue
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read().strip()

    def read_stdin():
        raw = sys.stdin.buffer.read()
        for enc in ['utf-8', 'gbk', 'gb2312', 'utf-8-sig']:
            try:
                return raw.decode(enc).strip()
            except UnicodeDecodeError:
                continue
        return raw.decode('utf-8', errors='replace').strip()

    if len(sys.argv) >= 3:
        user_input = read_file(sys.argv[2])
    elif not sys.stdin.isatty():
        user_input = read_stdin()
    else:
        print(f"模式: {mode}")
        print("粘贴内容后按 Ctrl+Z 然后回车:\n")
        user_input = read_stdin()

    if not user_input:
        print("没有输入内容")
        sys.exit(1)

    print(f"\n{'='*50}")
    print(f"AI 处理中 ({mode})...")
    print(f"{'='*50}\n")

    try:
        result = chat(MODES[mode], user_input)
        print(result)
        print(f"\n{'='*50}")
        print("完成")
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
