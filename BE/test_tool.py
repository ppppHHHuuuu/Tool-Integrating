import asyncio
from concurrent.futures import ThreadPoolExecutor
import sys
import os
import pathlib
import json
import time
from tools.Mythril import Mythril
from tools.Slither import Slither
# from tools.Slither import Slither
from tools.Tool import Tool

from tools.type import ToolName
from tools.utils.parsers import obj_to_jsonstr
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# start = time.time()
# result = [t for t in (Tool.analyze_files_async(
#     sub_container_file_path=r'user1/contract',
#     files_names=['swc-107.sol']*1,
#     tools=[ToolName.Mythril]
# ))]
# end = time.time()

# print(end - start)
# print(result)
directory = os.path.join(os.path.dirname(__file__), 'tools', 'storage', 'user1', 'contracts')
file_names = [file_name for file_name in os.listdir(directory)]

# File lưu ở thư mục storage
print(obj_to_jsonstr(Tool.run_tools_async(
    sub_container_file_path="user1/contracts",
    
    file_name= "swc-107-simple-dao.sol",
)))