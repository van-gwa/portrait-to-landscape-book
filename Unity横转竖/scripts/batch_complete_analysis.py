#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量处理所有预制体 - 生成完整分析笔记
"""

import os
import sys
from pathlib import Path
from datetime import datetime

PREFABS_DIR = r"D:\CursorProject\Dadian\Arts\Assets\ArtResources\UIs\Prefabs"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"

# 动态导入脚本
sys.path.insert(0, os.path.join(VAULT_DIR, 'scripts'))
from extract_complete_prefab import CompleteAnalyzer

def batch_process(start_index=0, limit=None, module_filter=None):
    """批量处理预制体"""
    # 找所有预制体
    prefabs = []
    for root, dirs, files in os.walk(PREFABS_DIR):
        for file in files:
            if file.endswith('.prefab'):
                prefab_path = os.path.join(root, file)
                prefabs.append(prefab_path)

    prefabs = sorted(prefabs)

    # 过滤
    if module_filter:
        prefabs = [p for p in prefabs if module_filter in p]
        print("[Filter] Keeping {} prefabs from module '{}'".format(len(prefabs), module_filter))

    # 限制
    if limit:
        prefabs = prefabs[start_index:start_index + limit]
    else:
        prefabs = prefabs[start_index:]

    print("[Info] Processing {} prefabs".format(len(prefabs)))
    print("[Info] Estimated time: {:.1f} minutes".format(len(prefabs) * 0.5 / 60))

    analyzer = CompleteAnalyzer()
    success = 0
    failed = 0

    start_time = datetime.now()

    for i, prefab_path in enumerate(prefabs, 1):
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = os.path.relpath(prefab_path, PREFABS_DIR)

        # 每50个打印一次进度
        if i % 50 == 1 or i == len(prefabs):
            elapsed = (datetime.now() - start_time).total_seconds()
            rate = elapsed / max(i-1, 1)
            remaining = rate * (len(prefabs) - i)
            print("[Progress] [{}/{}] Elapsed: {:.0f}s, Remaining: {:.0f}s".format(
                i, len(prefabs), elapsed, remaining))

        # 处理
        try:
            if analyzer.process(prefab_path):
                success += 1
            else:
                failed += 1
        except Exception as e:
            print("[Error] {}: {}".format(rel_path, str(e)[:50]))
            failed += 1

    # 统计
    total_time = (datetime.now() - start_time).total_seconds()

    print("")
    print("=" * 60)
    print("COMPLETED")
    print("  Success: {}/{}".format(success, len(prefabs)))
    print("  Failed: {}/{}".format(failed, len(prefabs)))
    print("  Total time: {:.0f}s ({:.1f} min)".format(total_time, total_time/60))
    print("  Average: {:.2f}s per prefab".format(total_time/max(len(prefabs), 1)))
    print("=" * 60)

    return success, failed


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Batch process prefabs for complete analysis"
    )

    parser.add_argument('--start', type=int, default=0, help='Start index')
    parser.add_argument('--limit', type=int, help='Max prefabs to process')
    parser.add_argument('--module', help='Only process specific module')

    args = parser.parse_args()

    batch_process(
        start_index=args.start,
        limit=args.limit,
        module_filter=args.module
    )


if __name__ == "__main__":
    main()
