"""
Python 工程化基础：日志、配置、命令行参数。

运行方式：
    python 12_project_engineering/001_logging_config_cli.py --name cjh --debug
"""

import argparse
import logging
import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    """
    应用配置对象。

    把配置集中成对象，能减少到处读取环境变量或硬编码字符串的问题。
    """

    app_name: str
    debug: bool
    greeting_prefix: str


def load_config(debug: bool) -> AppConfig:
    """
    加载配置。

    这里演示常见优先级：命令行参数优先，其次环境变量，最后使用默认值。
    """

    return AppConfig(
        app_name=os.getenv("APP_NAME", "study-python"),
        debug=debug,
        greeting_prefix=os.getenv("GREETING_PREFIX", "Hello"),
    )


def setup_logging(debug: bool) -> None:
    """
    初始化日志配置。

    logging 比 print 更适合项目代码，因为它能区分日志级别，也方便输出到文件或日志系统。
    """

    level = logging.DEBUG if debug else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def parse_args() -> argparse.Namespace:
    """
    解析命令行参数。

    argparse 是标准库，适合写轻量级 CLI 工具，不需要额外安装依赖。
    """

    parser = argparse.ArgumentParser(description="日志、配置、命令行参数示例")

    parser.add_argument(
        "--name",
        default="world",
        help="要问候的名字，默认是 world",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="开启 debug 日志",
    )

    return parser.parse_args()


def build_message(config: AppConfig, name: str) -> str:
    """根据配置和用户输入构造输出内容。"""

    return f"{config.greeting_prefix}, {name}! Welcome to {config.app_name}."


def main() -> None:
    """程序入口：解析参数、加载配置、初始化日志、执行业务逻辑。"""

    args = parse_args()
    config = load_config(debug=args.debug)
    setup_logging(debug=config.debug)

    logger = logging.getLogger(__name__)
    logger.debug("当前配置: %s", config)

    message = build_message(config=config, name=args.name)

    logger.info("生成问候语成功")
    print(message)


if __name__ == "__main__":
    main()
